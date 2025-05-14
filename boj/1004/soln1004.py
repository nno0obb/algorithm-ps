"""
# 백준
# No. 1004 
# Python 3.11.11
# by "nno0obb"
"""

from math import sqrt


def main():
    # Input
    T = int(input())
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        planets = []
        for _ in range(n):
            cx, cy, r = map(int, input().split())
            planets.append((cx, cy, r))

        # Logic
        ans = 0
        for cx, cy, r in planets:
            # dx = (출발점 or 도착점 ~ 행성계) 거리
            # dx - r > 0 = 행성계 밖에 존재
            # dx - r < 0 = 행성계 안에 존재
            d1 = sqrt((cx - x1) ** 2 + (cy - y1) ** 2)
            d2 = sqrt((cx - x2) ** 2 + (cy - y2) ** 2)
            if (d1 - r) * (d2 - r) < 0:  # 출발점과 도착점이 행성계의 안팎에 있으면 진입/이탈 필요
                ans += 1

        # Output
        print(ans)


if __name__ == "__main__":
    main()
