/*
// 백준
// No. 24228
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
	var N, R int
	fmt.Fscanln(reader, &N, &R)
	// 먼저 종류별로 1개씩 - N
	// 그다음 짝 1개를 맞춤 - N + 1
	// 최대한 짝을 맞추지 않게끔 뽑으면 - (R-1)*2

	// Logic
	ans := N + 1 + (R-1)*2
	// Output
	fmt.Fprintln(writer, ans)
}
