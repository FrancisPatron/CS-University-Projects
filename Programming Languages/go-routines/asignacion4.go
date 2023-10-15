package main

import (
	"errors"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type Result struct {
	index  int
	result string
}

type Job struct {
	task func() (string, error)
}

func main() {
	var tasks []func() (string, error)
	for i := 0; i < 200; i++ {
		tasks = append(tasks, cook)
	}

	results := concurrentRetry(tasks, 20, 2)

	for r := range results {
		fmt.Println("Results recieved from thread: ", r)
	}

}

func cook() (string, error) {
	//randomn time consuming task
	x := rand.Intn(100)
	duration := time.Duration(rand.Intn(1e3)) * time.Millisecond
	time.Sleep(duration)
	if x <= 50 {
		return "error", errors.New("Failed")
	}
	return "Completed", nil
}

func chef(ID int, threads <-chan Job, results chan<- Result, max_tries int, waitingFor *sync.WaitGroup) {
	//each chef will sequentally cook any avilable jobs
	//chef will cook untill threads is empty
	for len(threads) > 0 {
		job := <-threads
		waitingFor.Add(1)

		for current_try := 1; current_try <= max_tries; current_try++ {
			res, err := job.task()
			if err == nil {
				results <- Result{index: ID, result: res}
				break
			} else if current_try > 1 {
				results <- Result{index: ID, result: err.Error()}
			}
		}
		waitingFor.Done()
	}
}

/*tasks = slice of tasks to be done
concurrent = max of parallel tasks
retry = max number of attempts to do a task*/
func concurrentRetry(tasks []func() (string, error), max_chefs int, retry int) <-chan Result {
	//If this print & the one at the end are together, concurrentRetry
	//does not wait
	fmt.Println("Wait Check")
	threads := make(chan Job, len(tasks))
	results := make(chan Result, len(tasks))

	var waitingFor sync.WaitGroup

	//add all tasks into channel for the chefs to acces
	for _, task := range tasks {
		threads <- Job{task: task}
	}

	//start maximum number of chefs possible
	for x := 0; x < max_chefs; x++ {
		go chef(x, threads, results, len(tasks), &waitingFor)
	}

	//Function cannot wait!
	go func() {
		waitingFor.Wait()
		close(threads)
		close(results)
	}()

	fmt.Println("Wait Check")
	return results
}
