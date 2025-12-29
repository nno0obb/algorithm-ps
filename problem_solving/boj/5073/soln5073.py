"""
# 백준
# No. 5073
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    while True:
        a, b, c = map(int, input().split())
        if (a, b, c) == (0, 0, 0):
            break

        # Logic
        d, e, f = sorted([a, b, c])
        if d + e <= f:
            ans = "Invalid"
        elif d == e == f:
            ans = "Equilateral"
        elif d == e or e == f:
            ans = "Isosceles"
        else:
            ans = "Scalene"

        # Output
        print(ans)


if __name__ == "__main__":
    main()
