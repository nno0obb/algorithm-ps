"""
# 백준
# No. 2562
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    nums = [int(input()) for _ in range(9)]

    # Logic
    max_num = max(nums)
    max_idx = nums.index(max_num) + 1

    # Output
    print(max_num)
    print(max_idx)


if __name__ == "__main__":
    main()
