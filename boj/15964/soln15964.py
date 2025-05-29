"""
# 백준
# No. 15964 
# Python 3.11.9
# by "nno0obb"
"""


def at(a: int, b: int) -> int:
    return (a + b) * (a - b)


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    ans = at(A, B)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
