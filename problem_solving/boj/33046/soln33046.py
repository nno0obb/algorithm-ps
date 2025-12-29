"""
# 백준
# No. 33046
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    # Logic
    no = (A + B - 1 + C + D - 1) % 4 + 1

    # Output
    print(no)


if __name__ == "__main__":
    main()
