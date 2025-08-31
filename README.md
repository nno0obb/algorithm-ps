# algorithm-boj

# Redo

## leetcode

- [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters)
- [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/description/)
- [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/description/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/description/)
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [134. Gas Station](https://leetcode.com/problems/gas-station/description/)

# Init

## boj

```shell
$ cd boj
$ python3 init.py --no <NO>
```

# Test

## boj

```shell
$ cd boj
$ cat <NO>/inputs/input1 | python3 <NO>/soln<NO>.py
$ pytest runcase.py -v --no <NO>
$ pytest runcase.py -v --no <NO> --relative-error "10**-2"
```

## leetcode

```shell
$ cd leetcode
$ pytest sol<NO>.py -v
```

# ETC

## boj

### obsidian

```shell
$ cd boj
$ python3 obsidian.py --no <NO>
```
