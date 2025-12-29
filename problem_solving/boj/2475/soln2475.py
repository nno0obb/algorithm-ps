"""
# 백준
# No. 2475 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    uid = map(int, input().split())

    # Logic
    ans = sum(map(lambda x: x**2, uid)) % 10

    # Output
    print(ans)


if __name__ == "__main__":
    main()
