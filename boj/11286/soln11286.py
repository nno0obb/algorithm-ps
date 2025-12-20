"""
# 백준
# No. 11286
# Python 3.11.9
# by "nno0obb"
"""

import heapq
import sys


def main():
    # Input
    N = int(input())
    X = [int(sys.stdin.readline().strip()) for _ in range(N)]

    # Logic
    heqp = []
    for x in X:
        if x != 0:
            heapq.heappush(heqp, (abs(x), x))
        else:
            # Output
            if heqp:
                print(heapq.heappop(heqp)[1])
            else:
                print(0)


if __name__ == "__main__":
    main()
