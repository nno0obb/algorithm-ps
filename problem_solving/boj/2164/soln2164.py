"""
# 백준
# No. 2164
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N = int(input())

    # Logic
    deq = deque(range(1, N + 1))
    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    ans = deq[0]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
