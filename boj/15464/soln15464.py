"""
# 백준
# No. 15464
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Logic
    curr, prev = B.copy(), [-1] * N
    for _ in range(3):
        for i, j in zip(range(1, N + 1), A):
            prev[i - 1] = curr[j - 1]
        curr, prev = prev, [-1] * N

    # Output
    print(*curr, sep="\n")


if __name__ == "__main__":
    main()
