"""
# 백준
# No. 11094
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    C = [sys.stdin.readline().strip() for _ in range(N)]

    # Logic
    A = []
    for cmd in C:
        if cmd.startswith("Simon says"):
            A.append(cmd[len("Simon says") :])

    # Output
    print(*A, sep="\n")


if __name__ == "__main__":
    main()
