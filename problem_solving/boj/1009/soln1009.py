"""
# 백준
# No. 1009 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())

        # Logic
        ones = {
            1: [1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5],
            6: [6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1],
            0: [10],
        }[a % 10]

        ans = ones[(b - 1) % len(ones)]

        # Output
        print(ans)


if __name__ == "__main__":
    main()
