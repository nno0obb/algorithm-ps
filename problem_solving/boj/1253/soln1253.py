"""
# 백준
# No. 1253
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    A.sort()

    ans = 0
    for i in range(N):
        is_good = False

        # A[l] < A[r] < A[i]
        l, r = 0, i - 1
        while not is_good and l < r:
            s = A[l] + A[r]
            if s == A[i]:
                is_good = True
                break
            elif s < A[i]:
                l += 1
            else:
                r -= 1

        # A[i] < A[l] < A[r]
        l, r = i + 1, N - 1
        while not is_good and l < r:
            s = A[l] + A[r]
            if s == A[i]:
                is_good = True
                break
            elif s < A[i]:
                l += 1
            else:
                r -= 1

        # A[l] < A[i] < A[r]
        l, r = 0, N - 1
        while not is_good and (l < i) and (r > i):
            s = A[l] + A[r]
            if s == A[i]:
                is_good = True
                break
            elif s < A[i]:
                l += 1
            else:
                r -= 1

        if is_good:
            ans += 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
