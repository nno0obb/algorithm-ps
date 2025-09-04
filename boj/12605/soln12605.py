"""
# 백준
# No. 12605
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    for i in range(1, N + 1):
        S = input()

        # Logic
        ans = f"Case #{i}: " + " ".join(S.split()[::-1])

        # Output
        print(ans)


if __name__ == "__main__":
    main()
