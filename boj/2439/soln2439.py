"""
# 백준
# No. 2439
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic, Output
    for i in range(1, N + 1):
        print(" " * (N - i) + "*" * i)


if __name__ == "__main__":
    main()
