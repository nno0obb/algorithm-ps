"""
# 백준
# No. 2869
# Python 3.11.11
# by "nno0obb"
"""


def main():
    # Input
    A, B, V = map(int, input().split())

    # Logic
    ans = ((V - A) + (A - B - 1)) // (A - B) + 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
