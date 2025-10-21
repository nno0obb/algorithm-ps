/*
// 백준
// No. 1002
// Go 1.24.8
// by "nno0obb"
*/

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func logic(x1, y1, r1, x2, y2, r2 int) int {
	d := math.Sqrt(math.Pow(float64(x1-x2), 2) + math.Pow(float64(y1-y2), 2))
	if d == 0 {
		if r1 == r2 {
			return -1
		} else {
			return 0
		}
	} else {
		if float64(r1+r2) < d {
			return 0
		} else if float64(r1+r2) == d {
			return 1
		} else if math.Abs(float64(r1-r2)) < d && d < float64(r1+r2) {
			return 2
		} else if math.Abs(float64(r1-r2)) == d {
			return 1
		} else {
			return 0
		}
	}
}

func main() {
	defer writer.Flush()

	// Input
	var T int
	fmt.Fscanln(reader, &T)
	for range T {
		var x1, y1, r1, x2, y2, r2 int
		fmt.Fscanln(reader, &x1, &y1, &r1, &x2, &y2, &r2)

		// Logic
		ans := logic(x1, y1, r1, x2, y2, r2)

		// Output
		fmt.Fprintln(writer, ans)
	}
}
