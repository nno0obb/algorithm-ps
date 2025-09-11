"""
# 백준
# No. 1233
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    S1, S2, S3 = map(int, input().split())

    # Logic
    counter = Counter()
    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                counter[i + j + k] += 1

    ans = counter.most_common(1)[0][0]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
