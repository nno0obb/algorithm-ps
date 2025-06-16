"""
# 백준
# No. 1411 
# Python 3.11.9
# by "nno0obb"
"""


def is_숌(w1, w2) -> bool:
    trans = {}
    for c1, c2 in zip(w1, w2):
        if c1 in trans:
            if trans[c1] != c2:
                return False
        elif c2 in trans.values():
            return False
        else:
            trans[c1] = c2
    return True


def main():
    # Input
    N = int(input())
    words = [input() for _ in range(N)]

    # Logic
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            w1, w2 = words[i], words[j]
            if is_숌(w1, w2):
                ans += 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
