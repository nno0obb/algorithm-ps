"""
# 백준
# No. 1292 
# Python 3.11.9
# by "nno0obb"
"""


def easy_sum(n: int) -> int:
    s, cnt = 0, 0
    for i in range(1, 1000 + 1):
        if cnt + i < n:
            s += i * i
            cnt += i
        else:
            s += i * (n - cnt)
            break
    return s


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    ans = easy_sum(B) - easy_sum(A - 1)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
