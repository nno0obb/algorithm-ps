"""
# 백준
# No. 2659
# Python 3.11.9
# by "nno0obb"
"""

from itertools import product


def get_clock_num(selected_nums):
    cands = [
        selected_nums[0:] + selected_nums[:0],
        selected_nums[1:] + selected_nums[:1],
        selected_nums[2:] + selected_nums[:2],
        selected_nums[3:] + selected_nums[:3],
    ]
    clock_num = float("inf")
    for cand in cands:
        clock_num = min(clock_num, int("".join(map(str, cand))))
    return clock_num


def main():
    # Input
    target_nums = list(map(int, input().split()))

    # Logic
    clock_nums = set()
    for selected_nums in product(range(1, 10), repeat=4):
        clock_num = get_clock_num(selected_nums)
        clock_nums.add(clock_num)
    clock_nums = list(sorted(clock_nums))

    target_clock_num = get_clock_num(target_nums)
    ans = clock_nums.index(target_clock_num) + 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
