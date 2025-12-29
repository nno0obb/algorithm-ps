"""
# 백준
# No. 4884
# Python 3.11.9
# by "nno0obb"
"""

from math import ceil, log


def main():
    # Input
    while True:
        G, T, A, D = map(int, input().split())
        if (G, T, A, D) == (-1, -1, -1, -1):
            break

        # Logic
        I = G * (T * (T - 1) // 2)  # 토너먼트
        J = 2 ** ceil(log(G * A + D, 2))  # 가까운 2의 제곱
        X = I + (J - 1)  # 총 열리는 경기 수
        Y = J - (G * A + D)  # 추가해야하는 팀의 수

        # Output
        print(f"{G}*{A}/{T}+{D}={X}+{Y}")


if __name__ == "__main__":
    main()
