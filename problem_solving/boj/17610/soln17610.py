"""
# 백준
# No. 17610 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    K = int(input())
    G = list(map(int, input().split()))

    # Logic
    S = sum(G)
    C = set([G[0], -G[0], 0])
    for g in G[1:]:
        N = set()
        for c in C:
            N.add(c + g)
            N.add(c)
            N.add(c - g)
        C = N

    P = list(filter(lambda x: x > 0, C))
    ans = S - len(P)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
