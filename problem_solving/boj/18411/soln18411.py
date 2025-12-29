"""
# 백준
# No. 18411
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B, C = map(int, input().split())

    # Logic
    ans = sum([A, B, C]) - min([A, B, C])

    # Output
    print(ans)


if __name__ == "__main__":
    main()
