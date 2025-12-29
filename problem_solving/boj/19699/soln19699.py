"""
# 백준
# No. 19699
# Python 3.11.9
# by "nno0obb"
"""

from itertools import combinations


def main():
    # Input
    N, M = map(int, input().split())
    H = list(map(int, input().split()))

    # Logic
    sums = [sum(comb) for comb in combinations(H, M)]
    sums = list(set(sums))

    ans = []
    for _sum in sums:
        i, is_prime = 2, True
        while i * i <= _sum:
            if _sum % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            ans.append(_sum)

    # Output
    if ans:
        print(*ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
