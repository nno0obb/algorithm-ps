"""
# 백준
# No. 20309
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    raw_evens, raw_odds = A[::2], A[1::2]
    A.sort()
    sorted_evens, sorted_odds = A[::2], A[1::2]

    ans = "NO"
    if sum(raw_evens) == sum(sorted_evens):
        if sum(raw_odds) == sum(sorted_odds):
            ans = "YES"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
