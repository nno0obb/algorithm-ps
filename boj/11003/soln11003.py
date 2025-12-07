"""
# 백준
# No. 11003
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    deq = deque()
    for i, num in enumerate(A):
        while deq and deq[-1][1] > num:
            deq.pop()
        deq.append((i, num))
        if i - deq[0][0] >= L:
            deq.popleft()

        # Output
        print(deq[0][1], end=" ")

    # Hint
    # Monotone Deque(모노톤 덱)


if __name__ == "__main__":
    main()
