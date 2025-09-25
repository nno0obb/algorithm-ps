"""
# 백준
# No. 31306
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    S = input()

    # Logic
    counter = Counter(S)

    cnt_a = counter.get("a", 0)
    cnt_e = counter.get("e", 0)
    cnt_i = counter.get("i", 0)
    cnt_o = counter.get("o", 0)
    cnt_u = counter.get("u", 0)
    cnt_y = counter.get("y", 0)

    ans_1 = cnt_a + cnt_e + cnt_i + cnt_o + cnt_u
    ans_2 = ans_1 + cnt_y

    # Output
    print(ans_1, ans_2)


if __name__ == "__main__":
    main()
