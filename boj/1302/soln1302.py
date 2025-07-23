"""
# 백준
# No. 1302
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    N = int(input())
    books = [input() for _ in range(N)]

    # Logic
    counter = Counter(sorted(books))
    most_common = counter.most_common(1)[0]

    # Output
    print(most_common[0])


if __name__ == "__main__":
    main()
