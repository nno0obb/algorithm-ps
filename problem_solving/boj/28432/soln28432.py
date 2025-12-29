"""
# 백준
# No. 28432
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    Ss = [input() for _ in range(N)]
    M = int(input())
    As = [input() for _ in range(M)]

    # Logic
    if N == 1 and M == 1:
        ans = As[0]
    else:
        idx = Ss.index("?")
        ans = -1
        for word in set(As) - set(Ss):
            if idx == 0:
                if word[-1] == Ss[idx + 1][0]:
                    ans = word
                    break
            elif idx == N - 1:
                if word[0] == Ss[idx - 1][-1]:
                    ans = word
                    break
            else:
                if word[0] == Ss[idx - 1][-1] and word[-1] == Ss[idx + 1][0]:
                    ans = word
                    break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
