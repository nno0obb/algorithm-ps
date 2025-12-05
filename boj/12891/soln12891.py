"""
# 백준
# No. 12891
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter
from operator import itemgetter


def main():
    # Input
    S, P = map(int, input().split())
    DNA = input()
    A, C, G, T = map(int, input().split())

    # Logic
    ans, counter = 0, Counter(DNA[: P - 1])
    for i in range(P - 1, S):
        counter[DNA[i]] += 1
        if all(x >= y for x, y in zip(itemgetter("A", "C", "G", "T")(counter), (A, C, G, T))):
            ans += 1
        counter[DNA[i - P + 1]] -= 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
