"""
# 백준
# No. 1920
# Python 3.11.9
# by "nno0obb"
"""

from bisect import bisect_right


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    # Logic
    A.sort()
    C = []
    for b in B:
        idx = bisect_right(A, b)
        if idx > 0 and A[idx - 1] == b:
            C.append(1)
        else:
            C.append(0)

    # Output
    print(*C, sep="\n")


if __name__ == "__main__":
    main()
