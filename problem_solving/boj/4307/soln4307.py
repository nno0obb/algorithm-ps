"""
# 백준
# No. 4307
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    T = int(input())
    for _ in range(T):
        L, N = map(int, sys.stdin.readline().strip().split())
        A = [int(sys.stdin.readline().strip()) for _ in range(N)]

        # Logic
        A.sort()
        min_time, max_time = -1, -1
        for a in A:
            min_time = max(min_time, min(a, L - a))
            max_time = max(max_time, a, L - a)

        # Output
        print(min_time, max_time)

        # Hint
        #  →     ←   ←
        # |a-----a---a|
        # |-a---a---a-|
        # |--a-a---a--|
        # |---a---a---|
        # |--a-a-a----|
        # |-a---a-----|
        # |a---a-a----|
        # |---a---a---|
        # |--a-----a--|
        # |-a-------a-|
        # |a---------a|
        # |-----------|


if __name__ == "__main__":
    main()
