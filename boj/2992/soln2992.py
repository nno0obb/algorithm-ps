"""
# 백준
# No. 2992
# Python 3.11.9
# by "nno0obb"
"""

from itertools import permutations


def main():
    # Input
    X = int(input())

    # Logic
    cands = set()
    for permutation in permutations(str(X)):
        cands.add(int("".join(permutation)))
    cands = list(sorted(cands))
    idx = cands.index(X)
    ans = cands[idx + 1] if idx + 1 < len(cands) else 0

    # Output
    print(ans)


if __name__ == "__main__":
    main()
