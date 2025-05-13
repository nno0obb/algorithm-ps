"""
# 백준
# No. 2775
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Logic
    # (a, b)   = (a-1, 1) + (a-1, 2) + ... + (a-1, b-1) + (a-1, b)
    # (a, b-1) = (a-1, 1) + (a-1, 2) + ... + (a-1, b-1)
    # (a, b)   = (a, b-1) + (a-1, b)

    max_k, max_n = 14, 14
    apt = [[0 for _ in range(max_n + 1)] for _ in range(max_k + 1)]
    for i in range(1, max_n + 1):
        apt[0][i] = i
    for i in range(1, max_k + 1):
        for j in range(1, max_n + 1):
            apt[i][j] = apt[i][j - 1] + apt[i - 1][j]

    # Input
    T = int(input())
    for _ in range(T):
        k, n = int(input()), int(input())

        # Logic
        ans = apt[k][n]

        # Output
        print(ans)


if __name__ == "__main__":
    main()
