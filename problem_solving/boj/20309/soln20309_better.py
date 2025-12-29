"""
# 백준
# No. 20309
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    ans = "YES"
    for idx, num in enumerate(A):
        if idx % 2 == 0:
            if num % 2 == 0:
                ans = "NO"
                break
        if idx % 2 == 1:
            if num % 2 == 1:
                ans = "NO"
                break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
