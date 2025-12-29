"""
# 백준
# No. 17626
# Python 3.11.9
# by "nno0obb"
"""

from math import sqrt


def main():
    # Input
    N = int(input())

    # Logic
    A = list(range(0, int(sqrt(N)) + 1))
    set_1 = set()
    for a in A:
        set_1.add(a * a)
    set_2 = set()
    for s1 in set_1:
        for s2 in set_1:
            set_2.add(s1 + s2)
    set_3 = set()
    for s1 in set_1:
        for s2 in set_2:
            set_3.add(s1 + s2)

    ans = 4
    if N in set_1:
        ans = 1
    elif N in set_2:
        ans = 2
    elif N in set_3:
        ans = 3

    # Output
    print(ans)


if __name__ == "__main__":
    main()
