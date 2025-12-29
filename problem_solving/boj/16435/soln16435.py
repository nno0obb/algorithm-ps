"""
# 백준
# No. 16435
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, L = map(int, input().split())
    H = list(map(int, input().split()))

    # Logic
    H.sort()
    for h in H:
        if h <= L:
            L += 1
        else:
            break

    # Output
    print(L)


if __name__ == "__main__":
    main()
