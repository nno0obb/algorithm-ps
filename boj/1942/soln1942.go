/*
// 백준
// No. 1942
// Go 1.24.8
// by "nno0obb"
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	// Input
	for range 3 {
		var start, end string
		fmt.Fscanln(reader, &start, &end)

		// Logic
		startTime, _ := time.Parse("15:04:05", start)
		endTime, _ := time.Parse("15:04:05", end)
		if startTime.After(endTime) {
			endTime = endTime.Add(24 * time.Duration(time.Hour))
		}

		ans, currTime := 0, startTime
		for currTime.Before(endTime) || currTime.Equal(endTime) {
			num, _ := strconv.Atoi(currTime.Format("150405"))
			if num%3 == 0 {
				ans++
			}
			currTime = currTime.Add(time.Second)
		}

		// Output
		fmt.Fprintln(writer, ans)
	}
}
