"""
# 백준
# No. 16675
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    ML, MR, TL, TR = input().split()

    # Logic
    ans = "?"

    if ML == MR:
        if ML == "S" and "R" in [TL, TR]:
            ans = "TK"
        elif ML == "R" and "P" in [TL, TR]:
            ans = "TK"
        elif ML == "P" and "S" in [TL, TR]:
            ans = "TK"

    if TL == TR:
        if TL == "S" and "R" in [ML, MR]:
            ans = "MS"
        elif TL == "R" and "P" in [ML, MR]:
            ans = "MS"
        elif TL == "P" and "S" in [ML, MR]:
            ans = "MS"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
