"""
# 백준
# No. 3052
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    nums = [int(input()) for _ in range(10)]

    # Logic
    mods = [num % 42 for num in nums]
    ans = len(set(mods))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
