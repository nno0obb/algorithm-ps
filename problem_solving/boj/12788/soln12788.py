"""
# 백준
# No. 12788
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    M, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    A.sort(reverse=True)

    ans, cnt = "STRESS", 0
    for i in range(len(A)):
        cnt += A[i]
        if cnt >= M * K:
            ans = i + 1
            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
