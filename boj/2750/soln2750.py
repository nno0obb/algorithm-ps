"""
# 백준
# No. 2750
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # Logic
    A.sort()

    # Output
    print(*A, sep="\n")


if __name__ == "__main__":
    main()
