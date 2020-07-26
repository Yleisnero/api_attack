package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"sync"
	"strconv"
)

func main() {
	host := os.Args[1]
	workers, err := strconv.Atoi(os.Args[2])

	if err != nil {
		fmt.Println(err)
	}

	var wg sync.WaitGroup

	for i := 0; i < workers; i++ {
		fmt.Println("Starting Worker", i)
		wg.Add(1)
		go worker(&wg, i, host)
		fmt.Println("go")
	}

	fmt.Println("Waiting for Workers to finish")
	wg.Wait()
}

func worker(wg *sync.WaitGroup, id int, host string) {
	for i := 0; i < 10000; i++ {
		resp, err := http.Get(host)
		if err != nil {
			fmt.Println(err)
		}

		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)

		if err != nil {
			fmt.Println(err)
		}

		fmt.Println(string(body))
	}
}
