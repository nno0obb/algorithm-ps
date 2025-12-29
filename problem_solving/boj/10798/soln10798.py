"""
# 백준
# No. 10798
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    B = [input() for _ in range(5)]

    # Logic
    ans = ""
    for i in range(15):
        for j in range(5):
            if i < len(B[j]):
                ans += B[j][i]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
