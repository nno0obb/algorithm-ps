"""
# 백준
# No. 10250
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        H, W, N = map(int, input().split())

        # Logic
        floor = N % H if N % H else H
        room = (N - 1) // H + 1 if N % H else N // H

        # Output
        print(f"{floor}{room:02d}")


if __name__ == "__main__":
    main()
