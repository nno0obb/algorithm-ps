"""
# 백준
# No. 1546 
# Python 3.11.11
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    scores = list(map(int, input().split()))

    # Logic
    max_score = max(scores)
    new_avg = sum(scores) * 100 / max_score / N

    # Output
    print(new_avg)


if __name__ == "__main__":
    main()
