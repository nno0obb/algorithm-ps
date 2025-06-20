"""
# 백준
# No. 31048 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Logic
    max_N = 10
    A = list(range(0, max_N + 1))
    for i in range(2, max_N + 1):
        A[i] *= A[i - 1]
        A[i] %= 10

    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())

        # Output
        print(A[N])


if __name__ == "__main__":
    main()
