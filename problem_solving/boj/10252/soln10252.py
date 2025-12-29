"""
# 백준
# No. 10252
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        M, N = map(int, input().split())

        # Logic
        paths = []
        if M % 2 == 0:
            for i in range(M):
                for j in range(N):
                    if i % 2 == 0:
                        paths.append((i, j))
                    else:
                        paths.append((i, N - 1 - j))

        elif N % 2 == 0:
            for j in range(N):
                for i in range(M):
                    if j % 2 == 0:
                        paths.append((i, j))
                    else:
                        paths.append((M - 1 - i, j))
        else:
            for i in range(M):
                for j in range(N - 1):
                    if i % 2 == 0:
                        paths.append((i, j))
                    else:
                        paths.append((i, N - 2 - j))
            for i in range(M):
                paths.append((M - 1 - i, N - 1))

        # Output
        print(1)
        for path in paths:
            i, j = path
            print(f"({i},{j})")


if __name__ == "__main__":
    main()
