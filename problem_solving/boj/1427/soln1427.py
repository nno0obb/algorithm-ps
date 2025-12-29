"""
# 백준
# No. 1427
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = input()

    # Logic
    ans = "".join(sorted(N, reverse=True))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
