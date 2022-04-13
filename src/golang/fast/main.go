package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
	"runtime"
	"math"
)

func main() {
	start := time.Now()
	file, err := ioutil.ReadFile("../../rounds.txt");
	if err != nil {
		fmt.Println(err)
	}
	rounds, _ := strconv.Atoi(strings.TrimSpace(string(file)))

	total := make([]bool, rounds + 1)
	for l := 0; l <= rounds; l++ { total[l] = true }

	for i := 2; i < int(math.Sqrt(float64(rounds))); i++ {
		if total[i] {
			for j := i * i; j <= rounds; j += i {
				total[j] = false
			}
		}
	}

	primes := 0
	for k := 2; k < rounds; k++ {
		if total[k] {
			primes += 1
		}
	}


	end := time.Since(start)
	fmt.Println(runtime.Version()[2:], float64(end.Nanoseconds()) / 1e9)

}

