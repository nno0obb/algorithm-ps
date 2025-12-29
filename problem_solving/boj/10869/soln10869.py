"""
# 백준
# No. 10869 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    results = [A + B, A - B, A * B, *divmod(A, B)]

    # Output
    print(*results, sep="\n")


if __name__ == "__main__":
    main()
