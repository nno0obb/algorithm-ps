"""
# 백준
# No. 4344 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    C = int(input())
    for _ in range(C):
        N, *scores = map(int, input().split())

        # Logic
        avg = sum(scores) / N
        above_avg = [score for score in scores if score > avg]
        rate = len(above_avg) / N * 100

        # Output
        print(f"{rate}%")


if __name__ == "__main__":
    main()
