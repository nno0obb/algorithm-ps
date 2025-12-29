"""
# 백준
# No. 20336
# Python 3.11.9
# by "nno0obb"
"""

import random


def main():
    # Input
    N = int(input())
    menus = list(list(input().split()[1:]) for _ in range(N))

    # Logic
    choice = random.choice(menus)

    # Output
    print(len(choice))
    print(*choice, sep="\n")


if __name__ == "__main__":
    main()
