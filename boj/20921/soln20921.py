"""
# 백준
# No. 20921 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())

    # Logic
    ans, lst = [], []
    for k in range(N - 1, -1, -1):
        n = k + 1
        if K >= k:
            ans.append(n)
            K -= k
        else:
            lst.append(n)
    ans += lst[::-1]

    # Output
    print(*ans)


if __name__ == "__main__":
    main()


#  N=9,  K=7
# (n=,   k= ) - ans  / lst
# (n=9 , k=8) -      / [9]
# (n=8 , k=7) -      / [9, 8]
# (n=7 , k=6) -      / [9, 8, 7]
# (n=6 , k=5) -      / [9, 8, 7, 6]
# (n=5 , k=4) - 5    / [9, 8, 7, 6]
# (n=4 , k=3) - 5,   / [9, 8, 7, 6, 4]
# (n=3 , k=2) - 5, 3 / [9, 8, 7, 6, 4]
# (n=2 , k=1) - 5, 3 / [9, 8, 7, 6, 4, 2]
# (n=1 , k=0) - 5, 3 / [9, 8, 7, 6, 4, 2, 1]
