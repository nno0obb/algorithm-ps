"""
# 백준
# No. 4153
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    while True:
        a, b, c = map(int, input().split())

        if not all([a, b, c]):
            break

        # Logic
        d, e, f = sorted([a, b, c])
        is_right = (d**2 + e**2) == f**2

        # Output
        print("right" if is_right else "wrong")


if __name__ == "__main__":
    main()
