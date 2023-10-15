**CIIC 4082 – Arquitectura de Computadoras II** 

**Diseño de Aplicación con Manejo de Interrupciones y Temporizadores Cronómetro** 

**Introducción** 

El MSP430FR6989 Launchpad provee múltiples opciones para desarrollar aplicaciones.  Entre ellas se encuentra la pantalla LCD, el manejo de interrupciones y múltiples temporizadores (timers).  En esta actividad se diseñará e implementará una aplicación que hará uso estas tres herramientas.  

**Descripción General del Sistema**  

Se diseñará un sistema para implementar un cronómetro simple utilizando el MSP430FR6989 Launchpad.  El cronómetro tendrá dos dígitos para los segundos y dos dígitos para las centésimas de segundos.  Para presentar los cuatro dígitos se utilizarán los cuatro caracteres alfanuméricos de la extrema derecha del despliegue.  La siguiente figura muestra como luciría el valor 25.48 dentro de la organización del despliegue. 

![](Aspose.Words.4ddb0713-e030-49b0-92e6-eb2aa4d4c7ae.001.jpeg) 

**Operación del Sistema** 

Inicialmente en la pantalla aparecerá 00.00.  Al presionar el botón S1 el conteo de los segundos comenzará a incrementar.  Si se presiona S1 nuevamente el valor que se muestra en la pantalla se mantendrá fijo, pero internamente el contador seguirá corriendo.  Por ejemplo:  si estando en 00.00 presionamos S1 el contador comenzará a incrementar.  Si luego de 17.25 segundos presionamos S1 en el despliegue aparecerá de forma fija 17.25.  Si luego de 6 segundos presionamos S1 nuevamente entonces aparecerá en el despliegue 23.25 y el valor en pantalla seguirá incrementando.  Sea que el valor en pantalla esté incrementando o esté fijo, al presionar S2 el valor regresará a 00.00 y el contador se detendrá hasta que se presione nuevamente S1.  El conteo del cronómetro es circular, así que luego de 99.00 regresa a 00.00. 

**Requisitos Técnicos** 

Luego de la inicialización del sistema y que aparezca el 00.00 en el despliegue el MCU entrará en modo Low Power y sólo saldrá del mismo para atender subrutinas de manejo de interrupciones. Cuando el procesador no tenga tareas para realizar se mantendrá en modo Low Power. Las lecturas del estado de los botones se realizarán como atenciones a peticiones de interrupción que generarán los mismos.  No se leerán utilizando polling.  Todos los controles de tiempo en el sistema se realizarán utilizando el temporizador Timer\_A0.  No se implementarán por medio de estructuras iterativas. 

El programa tiene que ser modular dividido en subrutinas.  Cada subrutina terminará con un ret y en la medida en que sea posible operará sobre valores que recibirá por medio de registros o del stack. 

No se realizará brincos de una subrutina a otra por medio de instrucciones que no sean call. 

**Reporte** 

**Portada:** Título, curso, profesor, integrantes, fecha **Introducción:** Descripción general del producto.  1 página 

**Proceso de solución del problema:** Cómo se realizó el análisis del problema, se determinaron las tareas, qué tuvieron que buscar e investigar (con referencias). 1 a 3 páginas 

**Distribución de tareas:** Tabla mostrando las tareas que realizaron (investigaciones, pruebas, algoritmos, creación de código, etc.) y los integrantes del equipo a que realizaron las mismas. 

Ejemplo: 



|Tarea |Persona a cargo |Comentarios |
| - | - | - |
|Crear subrutina que recibe un dígito decimal en R5 y la posición del dígito en R6 y escribe presenta el mismo en el despliegue. |Pepito Pérez ||
||||
**Código del programa:** Copia del archivo con el código del programa.  Letra Courier New o Consolas 

**Notas:** El reporte se entregará en formato compatible con MS-Word (.docx o .doc).  El nombre del archivo con el reporte será CIIC4082ChronoGroup## en donde ## es el número del grupo utilizando dos dígitos.   

**Entrega de programa** 

**Documentación de las subrutinas** 

Objetivo: Propósito de la subrutina.  Debe hacer sólo una tarea 

Precondiciones: Lo que siempre tiene que ser cierto antes de la ejecución de la subrutina para que la misma funcione de manera correcta 

Postcondiciones: Lo que siempre será cierto luego de ejecutar la subrutina Autor/a:  Persona que diseñó la subrutina 

Fecha: Cuándo se creó esta versión de la subrutina 

**Ejemplo** 

;Objetivo: Convertir tres dígitos decimales individuales almacenados en R5, R6 y R7 (R5:R6:R7) en un entero de 16 bits 

;Precondiciones: El dígito que representa las centenas está almacenado en R5, las decenas en R6 y las unidades en R7 

;Postcondiciones: R8 contiene el valor entero representado por los dígitos individuales en R5, R6 y R7 ;Autor: Pepito Pérez 

;Fecha: 29/mar/20201 

Entregará el programa de la siguiente forma.  En un archivo de texto (.txt) tendrá el código completo del programa.  Este archivo se utilizará para copiar el código a un programa nuevo en el IAR y probar el funcionamiento.  Si el programa copiado de esta forma no funciona no recibe puntos en la tarea.  El nombre de este archivo será ChronoGroup## en donde donde ## es el número del grupo con dos dígitos.  En adición entregará el fólder que contiene todos los fólders y archivos de su workspace.  Comprimirá el fólder y el archivo tiempo texto en un solo archivo (.zip o .rar) con el nombre ChronoGroup## en donde ## es el número del grupo con dos dígitos. 

**Entrega de vídeo** 

**Vídeo de la operación de la aplicación**:  Muestra que el programa cumple con todos los requisitos.  Estado inicial con 00.00, efectos de presionar S1 en varias ocasiones, efecto de presionar S2 y luego nuevamente S1.  También mostrarán que luego de 99.99 regresa a 00.00.  Para esta parte pueden eliminar parte del vídeo.  Por ejemplo, contar hasta 20 segundos y luego brincar a 90 segundos. La duración máxima es de cuatro minutos, pero puede ser de mucho menos siempre que cumpla con mostrar el funcionamiento de las distintas opciones.  Tiene que comenzar mostrando cómo ejecutar el programa en el IDE y luego continuar mostrando sólo la operación en el Launchpad sin el IDE y luego de apagar y encender nuevamente el Launchpad.  Tome en consideración que es posible que el dispositivo que utilice para tomar el vídeo tenga más resolución de la que hace falta.  Así que verifique cuál es la resolución más baja con la cual puede tomar un vídeo que sea vea bien.  De esta forma el tamaño del archivo no será más grande de lo necesario.  El archivo tiene que estar en formato .mp4 y el nombre tiene que ser ChronoGroup## en donde ## es el número del grupo con dos dígitos. 

**Hoja de Autoevaluación y Evaluación de los Pares** 

Entregará el archivo de Excel completado.  El nombre del archivo será *SuNombreGroup##* en donde *SuNombre* es su primer nombre seguido de su primer apellido si espacios entre ellos.  No utilizará tildes, acentos, diéresis ni carácter alguno que no sea una letra.  No incluirá iniciales, ni segundo nombre ni sgundo apellido.  ## es el número de su grupo utilizando dos dígitos.  Por ejemplo, si usted pertenece al grupo 35 y su nombre es Rincón D. Mayagüez Añasco el nombre del archivo será RinconMayaguezGroup35. 
