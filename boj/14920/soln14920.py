"""
# 백준
# No. 14920
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    C, n = {}, 1
    C[n] = N
    while C[n] != 1:
        if C[n] % 2 == 0:
            n += 1
            C[n] = C[n - 1] // 2
        else:
            n += 1
            C[n] = 3 * C[n - 1] + 1

    # Output
    print(n)


if __name__ == "__main__":
    main()
