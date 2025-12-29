"""
# 백준
# No. 24060
# Python 3.11.9
# by "nno0obb"
"""

import sys

sys.setrecursionlimit(1_000_000)


# Global Variables
K = sys.maxsize
ans = -1
tmp = None


def merge_sort(A: list[int], p: int, r: int):
    global K

    if K == 0:
        return

    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A: list[int], p: int, q: int, r: int):
    global K, ans, tmp

    if K == 0:
        return

    i, j, t = p, q + 1, 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1

    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1

    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1

    i, t = p, 1
    while i <= r:
        A[i] = tmp[t]
        K -= 1
        if K == 0:
            ans = A[i]

        t += 1
        i += 1


def main():
    global K, tmp

    # Input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    A.insert(0, None)
    tmp = [0] * (N + 1)
    merge_sort(A, 1, N)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
