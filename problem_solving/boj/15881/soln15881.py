"""
# 백준
# No. 15881
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S = input()

    # Logic
    idx, cnt = 0, 0
    while True:
        idx = S.find("pPAp", idx)
        if idx == -1:
            break
        cnt += 1
        idx += 4

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
