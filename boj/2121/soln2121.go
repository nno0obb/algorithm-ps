/*
// 백준
// No. 2121
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

type Point struct {
	x int
	y int
}

func main() {
	defer writer.Flush()

	// Input
	var N int
	fmt.Fscanln(reader, &N)
	var A, B int
	fmt.Fscanln(reader, &A, &B)
	C := make(map[Point]bool)
	for range N {
		var x, y int
		fmt.Fscanln(reader, &x, &y)
		C[Point{x, y}] = true
	}

	// Logic
	var ans int
	for c := range C {
		if C[Point{c.x, c.y + B}] && C[Point{c.x + A, c.y}] && C[Point{c.x + A, c.y + B}] {
			ans++
		}
	}

	// Output
	fmt.Fprintln(writer, ans)
}
