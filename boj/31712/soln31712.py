"""
# 백준
# No. 31712
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    CU, DU = map(int, input().split())
    CD, DD = map(int, input().split())
    CP, DP = map(int, input().split())
    H = int(input())

    # Logic
    H -= DU + DD + DP
    cnt = 0
    while H > 0:
        cnt += 1
        if cnt % CU == 0:
            H -= DU
        if cnt % CD == 0:
            H -= DD
        if cnt % CP == 0:
            H -= DP

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
