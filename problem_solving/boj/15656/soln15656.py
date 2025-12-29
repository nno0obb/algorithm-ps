"""
# 백준
# No. 15656
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # Logic
    nums.sort()
    que = deque([[]])
    for _ in range(M):
        for _ in range(len(que)):
            seq = que.popleft()
            for num in nums:
                que.append(seq + [num])

    # Output
    for seq in que:
        print(*seq)


if __name__ == "__main__":
    main()
