"""
# 백준
# No. 1037 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    divisors = list(map(int, input().split()))

    # Logic
    divisors.sort()
    ans = divisors[0] * divisors[-1]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
