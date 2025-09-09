"""
# 백준
# No. 20125
# Python 3.11.9
# by "nno0obb"
"""

from collections import namedtuple
from itertools import product

Point = namedtuple("Point", ["x", "y"])


def main():
    # Input
    N = int(input())
    A = [["_"] * (N + 1)] + [list("_" + input()) for _ in range(N)]

    # Logic
    def get_next_point(cx, cy, dx, dy):
        nx, ny = cx + dx, cy + dy
        if 1 <= nx <= N and 1 <= ny <= N:
            if A[nx][ny] == "*":
                return Point(nx, ny)
        return None

    def get_points(point, dx, dy):
        points = [point]
        while True:
            next_point = get_next_point(points[-1].x, points[-1].y, dx, dy)
            if next_point:
                points.append(next_point)
            else:
                break
        return points

    head = None
    for x, y in product(range(N), range(N)):
        if A[x][y] == "*":
            head = Point(x, y)
            break

    heart = Point(head.x + 1, head.y)
    left_arm = get_points(Point(heart.x, heart.y - 1), dx=0, dy=-1)
    right_arm = get_points(Point(heart.x, heart.y + 1), dx=0, dy=+1)
    waist = get_points(Point(heart.x + 1, heart.y), dx=+1, dy=0)
    left_leg = get_points(Point(waist[-1].x + 1, waist[-1].y - 1), dx=+1, dy=0)
    right_leg = get_points(Point(waist[-1].x + 1, waist[-1].y + 1), dx=+1, dy=0)

    # Output
    print(heart.x, heart.y)
    print(len(left_arm), len(right_arm), len(waist), len(left_leg), len(right_leg))


if __name__ == "__main__":
    main()
