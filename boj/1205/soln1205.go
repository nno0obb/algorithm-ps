/*
// 백준
// No. 1205
// Go 1.24.8
// by "nno0obb"
*/

package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	// Input
	var N, S, P int
	fmt.Fscanln(reader, &N, &S, &P)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &A[i])
	}

	// Logic
	rank, idx := 1, 0
	for i := 0; i < N; i++ {
		if A[i] > S {
			rank += 1
			idx += 1
		} else if A[i] == S {
			idx += 1
		} else {
			break
		}
	}

	if idx >= P {
		rank = -1
	}

	// Output
	fmt.Fprintln(writer, rank)
}
