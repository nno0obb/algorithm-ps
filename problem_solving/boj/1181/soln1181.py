"""
# 백준
# No. 1181
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    words = [sys.stdin.readline().strip() for _ in range(N)]

    # Logic
    words = list(set(words))
    words.sort(key=lambda x: (len(x), x))

    # Output
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
