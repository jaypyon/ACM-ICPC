package main

import (
	. "fmt"
)

func main() {
	n, k := 0, 0
	coin := []int{}
	Scan(&n, &k)
	value := 0
	for i := 0; i < n; i++ {
		Scan(&value)
		coin = append(coin, value)
	}
	result := 0
	for i := len(coin) - 1; i >= 0; i-- {
		for {
			if k < coin[i] {
				break
			}
			coincnt := int(k / coin[i])
			result += coincnt
			k = k % coin[i]
		}

	}
	Print(result)
}
