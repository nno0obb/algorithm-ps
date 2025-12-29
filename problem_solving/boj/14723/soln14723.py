"""
# 백준
# No. 14723 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    a, b = 1, 1
    for _ in range(N - 1):
        if a == 1:
            a, b = b + 1, 1
        else:
            a, b = a - 1, b + 1

    # Output
    print(a, b)


if __name__ == "__main__":
    main()
