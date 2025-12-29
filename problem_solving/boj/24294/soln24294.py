"""
# 백준
# No. 24294
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    W1 = int(input())
    H1 = int(input())
    W2 = int(input())
    H2 = int(input())

    # Logic
    ans = 4 + 2 * (max(W1, W2) + (H1 + H2))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
