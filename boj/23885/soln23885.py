"""
# 백준
# No. 23885
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    # Logic
    ans = "NO"
    if sx == ex and sy == ey:
        ans = "YES"
    if (sx + sy) % 2 == (ex + ey) % 2:
        if N > 1 and M > 1:
            ans = "YES"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
