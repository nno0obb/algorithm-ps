"""
# 백준
# No. 2522
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic, Output
    for i in range(1, N):
        print(" " * (N - i) + "*" * i)
    print("*" * N)
    for i in range(1, N):
        print(" " * i + "*" * (N - i))


if __name__ == "__main__":
    main()
