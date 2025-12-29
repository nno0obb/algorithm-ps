"""
# 백준
# No. 2577
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    A = int(input())
    B = int(input())
    C = int(input())

    # Logic
    counter = Counter(str(A * B * C))

    # Output
    for i in range(10):
        print(counter[str(i)])


if __name__ == "__main__":
    main()
