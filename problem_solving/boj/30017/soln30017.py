"""
# 백준
# No. 30017
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    c1 = A + min(A - 1, B)  # more cheese
    c2 = B + min(A, B + 1)  # more patty
    ans = min(c1, c2)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
