"""
# 백준
# No. 15905
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]

    # Logic
    A.sort(key=lambda x: (-x[0], -x[1]))

    ans = 0
    for solved, penalty in A[5:]:
        if solved == A[5 - 1][0]:
            ans += 1
        else:
            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
