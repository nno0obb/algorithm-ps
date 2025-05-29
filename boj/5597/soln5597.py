"""
# 백준
# No. 5597 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = []
    for _ in range(28):
        n = int(input())
        N.append(n)

    # Logic
    B = set(range(1, 31)) - set(N)

    # Output
    print(min(B))
    print(max(B))


if __name__ == "__main__":
    main()
