"""
# 백준
# No. 6030
# Python 3.11.9
# by "nno0obb"
"""

from itertools import product


def main():
    # Input
    P, Q = map(int, input().split())

    # Logic
    PF, QF = set(), set()

    i = 1
    while i * i <= P:
        if P % i == 0:
            PF.add(i)
            PF.add(P // i)
        i += 1

    j = 1
    while j * j <= Q:
        if Q % j == 0:
            QF.add(j)
            QF.add(Q // j)
        j += 1

    # Output
    for p, q in product(sorted(PF), sorted(QF)):
        print(p, q)


if __name__ == "__main__":
    main()
