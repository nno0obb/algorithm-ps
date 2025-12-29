"""
# 백준
# No. 13410
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())

    # Logic
    ans = max([int(str(N * k)[::-1]) for k in range(1, K + 1)])

    # Output
    print(ans)


if __name__ == "__main__":
    main()
