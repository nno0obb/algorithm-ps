"""
# 백준
# No. 5874
# Python 3.11.9
# by "nno0obb"
"""

from bisect import bisect_left


def main():
    # Input
    S = input()

    # Logic
    X, idx = [], 0
    while True:
        x = S.find("((", idx)
        if x == -1:
            break
        X.append(x)
        idx = x + 1

    Y, idx = [], 0
    while True:
        y = S.find("))", idx)
        if y == -1:
            break
        Y.append(y)
        idx = y + 1

    ans = 0
    for x in X:
        idx = bisect_left(Y, x)
        ans += len(Y) - idx

    # Output
    print(ans)


if __name__ == "__main__":
    main()
