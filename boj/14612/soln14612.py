"""
# 백준
# No. 14612
# Python 3.11.9
# by "nno0obb"
"""

from functools import reduce


def main():
    # Input
    N, M = map(int, input().split())

    P = []
    for _ in range(N):
        cmd, *args = input().split()

        # Logic
        if cmd == "order":
            n, t = map(int, args)
            P.append((n, t))
        elif cmd == "sort":
            P.sort(key=lambda x: (x[1], x[0]))
        elif cmd == "complete":
            n = int(args[0])
            P = list(filter(lambda x, n=n: x[0] != n, P))

        # Output
        print(*reduce(lambda acc, x: acc + [x[0]], P, []) or ("sleep",))


if __name__ == "__main__":
    main()
