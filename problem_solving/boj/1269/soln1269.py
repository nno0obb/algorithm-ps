"""
# 백준
# No. 1269
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    len_A, len_B = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    # Logic
    C = A ^ B  # Symmetric Difference
    ans = len(C)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
