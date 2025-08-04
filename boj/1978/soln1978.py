"""
# 백준
# No. 1978
# Python 3.11.9
# by "nno0obb"
"""


def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def main():
    # Input
    N = int(input())
    nums = list(map(int, input().split()))

    # Logic
    cnt = 0
    for num in nums:
        if is_prime(num):
            cnt += 1

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
