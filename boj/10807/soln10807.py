"""
# 백준
# No. 10807 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))
    v = int(input())

    # Logic
    ans = A.count(v)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
