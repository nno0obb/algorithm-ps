"""
# 백준
# No. 32642
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    W = list(map(int, input().split()))

    # Logic
    ans = 0
    for i, w in enumerate(W):
        v = {1: +1, 0: -1}[w]
        ans += v * (N - i)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
