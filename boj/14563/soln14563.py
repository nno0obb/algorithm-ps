"""
# 백준
# No. 14563
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    Ns = list(map(int, input().split()))

    # Logic
    ans = []
    for N in Ns:
        divisors, i = [], 1
        while i < N:
            if N % i == 0:
                divisors.append(i)
            i += 1

        if sum(divisors) == N:
            ans.append("Perfect")
        elif sum(divisors) < N:
            ans.append("Deficient")
        elif sum(divisors) > N:
            ans.append("Abundant")

    # Output
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
