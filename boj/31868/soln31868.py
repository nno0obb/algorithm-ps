"""
# 백준
# No. 31868
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())

    # Logic
    ans = K // (2 ** (N - 1))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
