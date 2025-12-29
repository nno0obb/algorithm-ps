"""
# 백준
# No. 26517
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    k = int(input())
    a, b, c, d = map(int, input().split())

    # Logic
    left_val = a * k + b
    right_val = c * k + d
    continuity = left_val == right_val

    # Output
    if continuity:
        print("Yes", left_val)
    else:
        print("No")


if __name__ == "__main__":
    main()
