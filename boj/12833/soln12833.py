"""
# 백준
# No. 12833
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B, C = map(int, input().split())

    # Logic
    ans = A
    if C % 2:
        ans ^= B

    # Output
    print(ans)


if __name__ == "__main__":
    main()
