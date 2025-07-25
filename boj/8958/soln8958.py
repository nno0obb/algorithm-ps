"""
# 백준
# No. 8958
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        R = input()

        # Logic
        cnt, score = 0, 0
        for r in R:
            if r == "X":
                cnt = 0
            elif r == "O":
                cnt += 1
                score += cnt

        # Output
        print(score)


if __name__ == "__main__":
    main()
