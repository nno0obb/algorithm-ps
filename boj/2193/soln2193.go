/*
// 백준
// No. 2193
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
	var N int
	fmt.Fscanln(reader, &N)

	// Logic
	dp := make([][2]int, max(3, N+1))
	dp[1] = [2]int{0, 1}
	dp[2] = [2]int{1, 0}
	for i := 3; i <= N; i++ {
		dp[i][0] = dp[i-1][0] + dp[i-1][1]
		dp[i][1] = dp[i-1][0]
	}
	ans := dp[N][0] + dp[N][1]

	// Output
	fmt.Fprintln(writer, ans)
}
