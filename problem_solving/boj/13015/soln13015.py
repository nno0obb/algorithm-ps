"""
# 백준
# No. 13015
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    w, h = 4 * (N - 1) + 1, 2 * N - 1
    B = [[" " for _ in range(w)] for _ in range(h)]

    # First, Last
    for i in range(N):
        B[0][i] = "*"
        B[0][w - (i + 1)] = "*"
        B[h - 1][i] = "*"
        B[h - 1][w - (i + 1)] = "*"

    # Mid
    for i in range(1, N):
        B[i][i] = "*"
        B[i][i + N - 1] = "*"
        B[i][w - (i + 1)] = "*"
        B[i][w - (i + N)] = "*"
        B[h - (i + 1)][i] = "*"
        B[h - (i + 1)][i + N - 1] = "*"
        B[h - (i + 1)][w - (i + 1)] = "*"
        B[h - (i + 1)][w - (i + N)] = "*"

    # Output
    for row in B:
        print("".join(row).rstrip())


if __name__ == "__main__":
    main()
