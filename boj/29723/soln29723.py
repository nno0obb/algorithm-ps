"""
# 백준
# No. 29723
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M, K = map(int, input().split())
    SP = dict[str, int]()
    for _ in range(N):
        s, p = sys.stdin.readline().strip().split()
        SP[s] = int(p)
    T = [sys.stdin.readline().strip() for _ in range(K)]

    # Logic
    base = 0
    for t in T:
        if t in SP:
            base += SP[t]
            SP.pop(t)
            M -= 1

    ans = [base, base]
    if M > 0:
        ans[0] += sum(sorted(SP.values())[:M])
        ans[1] += sum(sorted(SP.values())[-M:])

    # Output
    print(*ans)


if __name__ == "__main__":
    main()
