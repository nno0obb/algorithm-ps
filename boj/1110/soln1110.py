"""
# 백준
# No. 1110 
# Python 3.11.9
# by "nno0obb"
"""


def cycle(n):
    a, b = divmod(n, 10)
    c = (a + b) % 10
    return b * 10 + c


def main():
    # Input
    N = int(input())

    # Logic
    cnt, now = 1, cycle(N)
    while N != now:
        now = cycle(now)
        cnt += 1

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
