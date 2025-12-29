"""
# 백준
# No. 1076
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    c1, c2, c3 = input(), input(), input()

    # Logic
    color = {
        "black": ("0", 1),
        "brown": ("1", 10),
        "red": ("2", 100),
        "orange": ("3", 1_000),
        "yellow": ("4", 10_000),
        "green": ("5", 100_000),
        "blue": ("6", 1_000_000),
        "violet": ("7", 10_000_000),
        "grey": ("8", 100_000_000),
        "white": ("9", 1_000_000_000),
    }

    ans = int(color[c1][0] + color[c2][0]) * color[c3][1]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
