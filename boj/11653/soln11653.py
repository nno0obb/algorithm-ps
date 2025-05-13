"""
# 백준
# No. 11653
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    f = 2
    while f * f <= N:  # <= sqrt(N)
        if N % f == 0:  # f is a factor of N
            N //= f

            # Output
            print(f)

        else:
            f += 1

    # Output
    if N > 1:
        print(N)  # N is prime number


if __name__ == "__main__":
    main()
