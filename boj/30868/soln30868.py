"""
# 백준
# No. 30868
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())

        # Logic
        votes = "++++ " * (N // 5) + "|" * (N % 5)
        votes = votes.strip()

        # Output
        print(votes)


if __name__ == "__main__":
    main()
