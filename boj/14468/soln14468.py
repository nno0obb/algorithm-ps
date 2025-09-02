"""
# 백준
# No. 14468
# Python 3.11.9
# by "nno0obb"
"""

from collections import defaultdict


def main():
    # Input
    S = input()

    # Logic
    cow = defaultdict(list)
    for idx, char in enumerate(S):
        cow[char].append(idx)

    ans = 0
    for u1 in range(ord("A"), ord("Z") + 1):
        for u2 in range(u1 + 1, ord("Z") + 1):
            c1, c2 = chr(u1), chr(u2)
            i1, i2 = cow[c1]
            j1, j2 = cow[c2]

            if i1 < j1 < i2 < j2:
                ans += 1
            elif j1 < i1 < j2 < i2:
                ans += 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
