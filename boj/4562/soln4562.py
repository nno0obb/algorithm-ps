"""
# 백준
# No. 4562
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    n = int(input())
    for _ in range(n):
        X, Y = map(int, input().split())

        # Logic, Output
        print("NO BRAINS" if X < Y else "MMM BRAINS")


if __name__ == "__main__":
    main()
