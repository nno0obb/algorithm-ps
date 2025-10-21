/*
// 백준
// No. 13877
// Go 1.24.8
// by "nno0obb"
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	// Input
	var T int
	fmt.Fscanln(reader, &T)
	for range T {
		var K, S string
		fmt.Fscanln(reader, &K, &S)

		// Logic
		_8, err := strconv.ParseInt(S, 8, 64)
		if err != nil {
			_8 = 0
		}
		_10, _ := strconv.ParseInt(S, 10, 64)
		_16, _ := strconv.ParseInt(S, 16, 64)

		// Output
		fmt.Fprintln(writer, K, _8, _10, _16)
	}
}
