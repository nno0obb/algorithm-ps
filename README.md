# algorithm-boj

# Redo

## leetcode

- [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters)
- [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/description/)
- [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/description/)

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
