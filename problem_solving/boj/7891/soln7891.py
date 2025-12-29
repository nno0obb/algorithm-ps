"""
# 백준
# No. 7891
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())

        # Logic, Output
        print(sum([A, B]))


if __name__ == "__main__":
    main()
