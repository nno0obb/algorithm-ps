"""
# 백준
# No. 32306
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    t1 = list(map(int, input().split()))
    t2 = list(map(int, input().split()))

    # Logic
    s1 = t1[0] * 1 + t1[1] * 2 + t1[2] * 3
    s2 = t2[0] * 1 + t2[1] * 2 + t2[2] * 3

    ans = 1 if s1 > s2 else 2 if s1 < s2 else 0

    # Output
    print(ans)


if __name__ == "__main__":
    main()
