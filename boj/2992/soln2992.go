/*
// 백준
// No. 2992
// Go 1.24.8
// by "nno0obb"
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func permutations(nums []int) []int {
	res := make(map[int]bool)
	used := make([]bool, len(nums))
	var curr []int

	var dfs func()
	dfs = func() {
		if len(curr) == len(nums) {
			cand := 0
			for _, num := range curr {
				cand = cand*10 + num
			}
			res[cand] = true
			return
		}
		for i := range len(nums) {
			if used[i] {
				continue
			}
			used[i] = true
			curr = append(curr, nums[i])
			dfs()
			used[i] = false
			curr = curr[:len(curr)-1]
		}
	}
	dfs()
	ret := []int{}
	for key := range res {
		ret = append(ret, key)
	}
	return ret
}

func main() {
	defer writer.Flush()

	// Input
	var X int
	fmt.Fscanln(reader, &X)

	// Logic
	nums := []int{}
	for _, x := range strconv.Itoa(X) {
		nums = append(nums, int(x-'0'))
	}

	perms := permutations(nums)
	sort.Ints(perms)
	idx := sort.SearchInts(perms, X)
	ans := 0
	if idx+1 < len(perms) {
		ans = perms[idx+1]
	}

	// Output
	fmt.Fprintln(writer, ans)
}
