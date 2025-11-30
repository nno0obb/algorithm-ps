"""
# 백준
# No. 10986
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    S = [0] * N
    S[0] = A[0] % M
    for i in range(1, N):
        S[i] = (S[i - 1] + A[i]) % M

    counter = Counter(S)
    counter[0] += 1
    ans = sum(v * (v - 1) // 2 for v in counter.values())

    # Output
    print(ans)


if __name__ == "__main__":
    main()
