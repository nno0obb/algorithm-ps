/*
// 백준
// No. 31668
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
	var N, M, K int
	fmt.Fscanln(reader, &N)
	fmt.Fscanln(reader, &M)
	fmt.Fscanln(reader, &K)

	// Logic
	ans := M / N * K

	// Output
	fmt.Fprintln(writer, ans)
}
