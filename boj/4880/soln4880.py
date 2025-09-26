"""
# 백준
# No. 4880
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    while True:
        a1, a2, a3 = map(int, input().split())
        if (a1, a2, a3) == (0, 0, 0):
            break

        # Logic
        _type, a4 = "??", -1
        if a2 - a1 == a3 - a2:
            _type, a4 = "AP", a3 + (a3 - a2)
        elif a2 / a1 == a3 / a2:
            _type, a4 = "GP", int(a3 * (a3 / a2))

        # Output
        print(f"{_type} {a4}")


if __name__ == "__main__":
    main()
