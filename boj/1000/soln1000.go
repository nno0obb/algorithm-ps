/*
// 백준
// No. 1000
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
	var A, B int
	fmt.Fscanln(reader, &A, &B)

	// Logic
	ans := A + B

	// Output
	fmt.Fprintln(writer, ans)
}
