"""
# BOJ
# No. 11653
# Python 3.10.4
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    f = 2
    while f * f <= N:
        if N % f == 0:
            N //= f

            # Output
            print(f)

        else:
            f += 1

            # Output
    if N > 1:
        print(N)  # prime


if __name__ == '__main__':
    main()
