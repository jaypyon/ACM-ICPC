package main

import (
	"bufio"
	. "fmt"
	"os"
	"sort"
)

var (
	N     int
	times [][]int
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	Fscanln(reader, &N)

	times = make([][]int, N)
	for i := 0; i < N; i++ {
		var a, b int
		Fscan(reader, &a, &b)
		times[i] = []int{a, b}
	}
	sort.Slice(times, func(a int, b int) bool {
		if times[a][1] == times[b][1] {
			return times[a][0] < times[b][0]
		}
		return times[a][1] < times[b][1]
	})
	now := 0
	rstcnt := 0
	for _, v := range times {
		if now <= v[0] {
			rstcnt++
			now = v[1]
		}
	}
	Fprint(writer, rstcnt)
}
