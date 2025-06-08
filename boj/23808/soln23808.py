"""
# 백준
# No. 23808 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    grid = [["@" for _ in range(N * 5)] for _ in range(N * 5)]
    for i in range(0, N * 2):
        for j in range(N * 1, N * 4):
            grid[i][j] = " "
    for i in range(N * 3, N * 4):
        for j in range(N * 1, N * 4):
            grid[i][j] = " "

    # Output
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main()
