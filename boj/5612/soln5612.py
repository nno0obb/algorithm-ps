"""
# 백준
# No. 5612
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    M = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]

    # Logic
    ans = M
    for i, o in A:
        if M >= 0:
            M += i
            M -= o
            ans = max(ans, M)
        else:
            ans, M = 0, 0
            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
