"""
# 백준
# No. 1205
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, S, P = map(int, input().split())
    A = []
    if N > 0:
        A = list(map(int, input().split()))

    # Logic
    rank, idx = 1, 0
    for i in range(N):
        if A[i] > S:
            rank += 1
            idx += 1
        elif A[i] == S:
            idx += 1
        else:
            break

    if idx >= P:
        rank = -1

    # Output
    print(rank)


if __name__ == "__main__":
    main()
