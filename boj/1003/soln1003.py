"""
# 백준
# No. 1003 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Logic
    max_N = 40
    f7i = [[0, 0] for _ in range(max_N + 1)]
    f7i[0] = [1, 0]
    f7i[1] = [0, 1]

    for i in range(2, max_N + 1):
        f7i[i][0] = f7i[i - 1][0] + f7i[i - 2][0]
        f7i[i][1] = f7i[i - 1][1] + f7i[i - 2][1]

    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())

        # Output
        print(f7i[N][0], f7i[N][1])


if __name__ == "__main__":
    main()
