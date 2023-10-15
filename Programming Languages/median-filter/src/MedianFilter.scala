import java.awt.Color
import java.io.File
import java.awt.image.BufferedImage
import akka.actor.{Actor, ActorSystem, Props}
import akka.pattern.ask
import MedianFilter.timeout
import akka.util.Timeout
import scala.concurrent.Await
import scala.concurrent.duration._
import javax.imageio.ImageIO

case class Serial(inputImage: BufferedImage)

class serialServer extends Actor {
  def receive: PartialFunction[Any, Unit] = {
    case Serial(inputImage) => {
      val startTime = System.currentTimeMillis()
      val filteredImage = serialFilter(inputImage)
      val endTime = System.currentTimeMillis() - startTime
      sender() ! (endTime, filteredImage)
    }

      def serialFilter(inputImage: BufferedImage): BufferedImage = {
        medianFilter(inputImage,1,inputImage.getWidth()-1,1,inputImage.getHeight()-1)
      }

  }
  def medianFilter(img: BufferedImage,left: Int, right: Int, up: Int, down: Int): BufferedImage = {
    // contains all RGB values of nearby pixels
    val neighbors = new Array[Color](9)
    // contains separate RGB values to sort & get medium
    val redValues, greenValues, blueValues = new Array[Int](9)

    for (x <- left until right){
      for ( y <- up until down){
        neighbors(0) = new Color(img.getRGB(x,y))
        neighbors(1) = new Color(img.getRGB(x+1,y+1))
        neighbors(2) = new Color(img.getRGB(x+1,y-1))
        neighbors(3) = new Color(img.getRGB(x-1,y-1))
        neighbors(4) = new Color(img.getRGB(x-1,y+1))
        neighbors(5) = new Color(img.getRGB(x,y-1))
        neighbors(6) = new Color(img.getRGB(x-1,y))
        neighbors(7) = new Color(img.getRGB(x+1,y))
        neighbors(8) = new Color(img.getRGB(x,y+1))

        for (i <- neighbors.indices) {
          redValues(i)=neighbors(i).getRed
          greenValues(i)=neighbors(i).getGreen
          blueValues(i)=neighbors(i).getBlue
        }
        //change RGB value
        img.setRGB(x,y,new Color(redValues.sortWith(_<_)(4),
              greenValues.sortWith(_<_)(4),
              blueValues.sortWith(_<_)(4)).getRGB)
      }
    }
    img
  }
}

class parallelServer extends Actor {
  def receive : PartialFunction[Any, Unit] = {
    case Serial(inputImage) => {
      val actorSystem3 = ActorSystem("ActorSystem3")
      val topLeft = actorSystem3.actorOf(Props(new topLeft()), name = "topLeft")
      val topRight = actorSystem3.actorOf(Props(new topRight()), name = "topRight")
      val botLeft = actorSystem3.actorOf(Props(new botLeft()), name = "botLeft")
      val botRight = actorSystem3.actorOf(Props(new botRight), name = "botRight")

      val startTime = System.currentTimeMillis()
      val topLeftFuture = topLeft ? Serial(inputImage)
      val topRightFuture = topRight ? Serial(inputImage)
      val botLeftFuture = botLeft ? Serial(inputImage)
      val botRightFuture = botRight ? Serial(inputImage)

      var result = Await.result(topLeftFuture, timeout.duration)
      result = Await.result(topRightFuture, timeout.duration)
      result = Await.result(botLeftFuture, timeout.duration)
      result = Await.result(botRightFuture, timeout.duration)

      val endTime = System.currentTimeMillis() - startTime
      actorSystem3.terminate()
      sender() ! (endTime, result)
    }
  }
  class topLeft extends Actor{
    def receive : PartialFunction[Any, Unit] = {
      case Serial(inputImage) =>
        val result = medianFilter(inputImage, 1,inputImage.getWidth()/2-1,1,inputImage.getHeight()/2-1)
        sender() ! result
    }
  }
  class topRight extends Actor{
    def receive : PartialFunction[Any, Unit] = {
      case Serial(inputImage) =>
        val result = medianFilter(inputImage,inputImage.getWidth()/2-1, inputImage.getWidth-1, 1, inputImage.getHeight()/2-1)
        sender() ! result
    }
  }
  class botRight extends Actor{
    def receive : PartialFunction[Any, Unit] = {
      case Serial(inputImage) =>
        val result = medianFilter(inputImage, inputImage.getWidth()/2-1, inputImage.getWidth-1,inputImage.getHeight()/2-1, inputImage.getHeight()-1)
        sender() ! result
    }
  }
  class botLeft extends Actor{
    def receive : PartialFunction[Any, Unit] = {
      case Serial(inputImage) =>
        val result = medianFilter(inputImage, 1, inputImage.getWidth/2-1,inputImage.getHeight()/2-1, inputImage.getHeight()-1)
        sender() ! result
    }
  }

  def medianFilter(img: BufferedImage,left: Int, right: Int, up: Int, down: Int): BufferedImage = {
    // contains all RGB values of nearby pixels
    val neighbors = new Array[Color](9)
    // contains separate RGB values to sort & get medium
    val redValues, greenValues, blueValues = new Array[Int](9)

    for (x <- left until right) {
      for (y <- up until down) {
        neighbors(0) = new Color(img.getRGB(x, y))
        neighbors(1) = new Color(img.getRGB(x + 1, y + 1))
        neighbors(2) = new Color(img.getRGB(x + 1, y - 1))
        neighbors(3) = new Color(img.getRGB(x - 1, y - 1))
        neighbors(4) = new Color(img.getRGB(x - 1, y + 1))
        neighbors(5) = new Color(img.getRGB(x, y - 1))
        neighbors(6) = new Color(img.getRGB(x - 1, y))
        neighbors(7) = new Color(img.getRGB(x + 1, y))
        neighbors(8) = new Color(img.getRGB(x, y + 1))

        for (i <- neighbors.indices) {
          redValues(i) = neighbors(i).getRed
          greenValues(i) = neighbors(i).getGreen
          blueValues(i) = neighbors(i).getBlue
        }
        //change RGB value
        img.setRGB(x, y, new Color(redValues.sortWith(_ < _)(4), greenValues.sortWith(_ < _)(4), blueValues.sortWith(_ < _)(4)).getRGB)
      }
    }
    img
  }
}

object MedianFilter extends App {
  var imagePath = io.StdIn.readLine("Enter the path of the image you want to filter:  ")
  val inputImage = ImageIO.read(new File(imagePath))
  implicit val timeout: Timeout = 500.seconds

  // System 1
  val actorSystem = ActorSystem("ActorSystem")
  val serialActor = actorSystem.actorOf(Props[serialServer], name = "serialActor")
  val serialFuture = serialActor ? Serial(inputImage)

  // System 2
  val actorSystem2 = ActorSystem("ActorSystem2")
  val parallelActor = actorSystem2.actorOf(Props[parallelServer], name = "parallelActor")
  val parallelFuture = parallelActor ? Serial(inputImage)

  // Results
  val parallel = Await.result(parallelFuture, timeout.duration)
  val serial = Await.result(serialFuture, timeout.duration)
  val outPathSerial = new File(imagePath.substring(0, imagePath.lastIndexOf('/')+1)+"serial.png")
  val outPathParallel = new File(imagePath.substring(0,imagePath.lastIndexOf('/')+1)+"parallel.png")

  serial match {
    case Tuple2(a: Any, b: Any) =>
      println("Serial Time:  " + a + " milliseconds")
      ImageIO.write(b.asInstanceOf[BufferedImage] , "png", outPathSerial)
    case _ => print("Error filtering image with serial")
  }
  parallel match {
    case Tuple2(a: Any, b: Any) =>
      println("Parallel Time:  " + a + " milliseconds")
      ImageIO.write(b.asInstanceOf[BufferedImage] , "png", outPathParallel)
    case _ => print("Error filtering image with parallel")
  }
  println("\nSerial Filtered Image saved at: "+outPathSerial)
  println("Parallel Filtered Image saved at: "+outPathParallel)
  actorSystem.terminate()
  actorSystem2.terminate()

}