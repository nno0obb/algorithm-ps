"""
# 백준
# No. 2023
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def is_prime(num: int) -> bool:
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

    # Logic
    n, primes = 1, deque([2, 3, 5, 7])
    while n < N:
        for _ in range(len(primes)):
            prime = primes.popleft()
            for digit in [1, 3, 7, 9]:
                cand = prime * 10 + digit
                if is_prime(cand):
                    primes.append(cand)
        n += 1

    # Output
    print(*primes, sep="\n")


if __name__ == "__main__":
    main()
