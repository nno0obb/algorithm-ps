"""
# 백준
# No. 24228
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, R = map(int, input().split())

    # Logic
    ans = N + 1 + (R - 1) * 2
    # 먼저 종류별로 1개씩 - N
    # 그다음 짝 1개를 맞춤 - N + 1
    # 최대한 짝을 맞추지 않게끔 뽑으면 - (R-1)*2

    # Output
    print(ans)


if __name__ == "__main__":
    main()
