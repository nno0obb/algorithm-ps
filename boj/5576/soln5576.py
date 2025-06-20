"""
# 백준
# No. 5576 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    W = [int(input()) for _ in range(10)]
    K = [int(input()) for _ in range(10)]

    # Logic
    W.sort(reverse=True)
    K.sort(reverse=True)

    ans = f"{sum(W[:3])} {sum(K[:3])}"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
