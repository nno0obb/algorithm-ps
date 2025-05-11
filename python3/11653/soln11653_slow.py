"""
# 백준
# No. 11653
# Python 3.11.11
# by "nno0obb"
# ver. slow
"""


def main():
    # Input
    N = int(input())

    # Logic
    f = 2
    while N > 1:
        if N % f == 0:
            N /= f

            # Output
            print(f)

        else:
            f += 1


if __name__ == "__main__":
    main()
