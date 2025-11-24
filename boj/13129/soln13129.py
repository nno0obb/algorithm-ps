"""
# 백준
# No. 13129
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B, N = map(int, input().split())

    # Logic
    C = [A * N + B * i for i in range(1, N + 1)]

    # Output
    print(*C)


if __name__ == "__main__":
    main()
