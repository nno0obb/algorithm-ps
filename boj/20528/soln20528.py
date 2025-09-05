"""
# 백준
# No. 20528
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S = input().split()

    # Logic
    S = [s[0] for s in S]
    ans = 1 if len(set(S)) == 1 else 0

    # Output
    print(ans)


if __name__ == "__main__":
    main()
