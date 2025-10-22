/*
// 백준
// No. 13311
// Go 1.24.8
// by "nno0obb"
*/

package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	// Logic
	ans := -1 // n ≡ a-1 ≡ -1 (mod a)

	// Output
	fmt.Fprintln(writer, ans)
}
