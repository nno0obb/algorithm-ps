"""
# 백준
# No. 11399
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    P = list(map(int, input().split()))

    # Logic
    P.sort()
    ans = 0
    for i, p in enumerate(P):
        ans += (N - i) * p

    # Output
    print(ans)


if __name__ == "__main__":
    main()
