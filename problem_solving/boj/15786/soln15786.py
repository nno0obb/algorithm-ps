"""
# 백준
# No. 15786
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())
    S = input()
    P = [input() for _ in range(M)]

    # Logic
    ans = []
    for p in P:
        idx = 0
        for c in p:
            if c == S[idx]:
                idx += 1
            if idx == N:
                break
        if idx == N:
            ans.append("true")
        else:
            ans.append("false")
    # Output
    print("\n".join(ans))


if __name__ == "__main__":
    main()
