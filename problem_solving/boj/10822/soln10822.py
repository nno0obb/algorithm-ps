"""
# 백준
# No. 10822
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    s = input()

    # Logic
    ans = sum(map(int, s.split(",")))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
