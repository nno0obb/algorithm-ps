"""
# 백준
# No. 2309 
# Python 3.11.11
# by "nno0obb"
"""


def main():
    # Input
    hs = [int(input()) for _ in range(9)]

    # Logic
    total = sum(hs)
    hs.sort()
    for i in range(9):
        for j in range(i + 1, 9):
            h1, h2 = hs[i], hs[j]
            if total - (h1 + h2) == 100:
                hs.remove(h1)
                hs.remove(h2)
                break
        if len(hs) == 7:
            break

    # Output
    print("\n".join(map(str, hs)))


if __name__ == "__main__":
    main()
