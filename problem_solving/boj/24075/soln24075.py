"""
# 백준
# No. 24075
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B = map(int, input().split())

    # Logic, Output
    print(max(A + B, A - B))
    print(min(A + B, A - B))


if __name__ == "__main__":
    main()
