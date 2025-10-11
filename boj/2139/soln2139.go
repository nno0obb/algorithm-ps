package main

import (
	"bufio"
	"fmt"
	"os"
	"testing"
	"time"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	// Input
	var day, month, year int
	for {
		fmt.Fscanln(reader, &day, &month, &year)
		if day == 0 && month == 0 && year == 0 {
			break
		}

		// Logic
		loc, _ := time.LoadLocation("Asia/Seoul")
		ans := time.Date(year, time.Month(month), day, 0, 0, 0, 0, loc).YearDay()

		// Output
		fmt.Fprintln(writer, ans)
	}
}

func test(t *testing.T) {

}
