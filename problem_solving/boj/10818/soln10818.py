"""
# 백준
# No. 10818
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    nums = list(map(int, input().split()))

    # Logic
    min_num = min(nums)
    max_num = max(nums)

    # Output
    print(min_num, max_num)


if __name__ == "__main__":
    main()
