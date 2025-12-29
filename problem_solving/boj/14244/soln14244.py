"""
# 백준
# No. 14244
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())

    # Logic
    edges = []
    for i in range(N - M + 1):
        edges.append((i, i + 1))
    for i in range(M - 2):
        edges.append((N - M, N - M + i + 2))

    # Output
    print("\n".join(f"{a} {b}" for a, b in edges))


if __name__ == "__main__":
    main()
