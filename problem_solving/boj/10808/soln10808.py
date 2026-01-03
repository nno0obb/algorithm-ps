"""
# 백준
# No. 10808
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    S = input()

    # Logic
    ans = [0] * (ord("z") - ord("a") + 1)
    for c in S:
        ans[ord(c) - ord("a")] += 1

    # Output
    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
