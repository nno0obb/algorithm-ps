"""
# 백준
# No. 25400
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    cnt = 0
    for i, num in enumerate(A):
        idx = i + 1 - cnt
        if idx != num:
            cnt += 1

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
