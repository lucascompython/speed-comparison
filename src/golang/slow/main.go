package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
	"runtime"
)

func main() {
	start := time.Now()
	file, err := ioutil.ReadFile("../../rounds.txt");
	if err != nil {
		fmt.Println(err)
	}
	rounds, _ := strconv.Atoi(strings.TrimSpace(string(file)))

	primes := 0
	composites := 0

	for num := 0; num < rounds; num++ {
		ctr := 0

		for i := 2; i < num / 2; i++ {
			if num % i == 0 {
				ctr++
				composites++
				break
			}
	}

		if ctr == 0 && num != 1{
			primes++
		}
	}
	end := time.Since(start)
	fmt.Println(runtime.Version()[2:], float64(end.Nanoseconds()) / 1e9)

}

