"""
# 백준
# No. 2738 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    C = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            C[i][j] = A[i][j] + B[i][j]

    # Output
    for c in C:
        print(*c)


if __name__ == "__main__":
    main()
