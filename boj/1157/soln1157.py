"""
# 백준
# No. 1157 
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    word = input()

    # Logic
    counter = Counter(word.upper())

    ans = counter.most_common(1)[0][0]

    if len(counter) > 1:
        _1st, _2nd = counter.most_common(2)
        if _1st[1] == _2nd[1]:
            ans = "?"
    # Output
    print(ans)


if __name__ == "__main__":
    main()
