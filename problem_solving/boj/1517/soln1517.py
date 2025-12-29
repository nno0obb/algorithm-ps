"""
# 백준
# No. 1517
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    tmp = [-1] * N
    ans = 0

    def merge_sort(s: int, e: int):
        nonlocal ans

        if s >= e:
            return

        m = (s + e) // 2
        merge_sort(s, m)
        merge_sort(m + 1, e)
        for i in range(s, e + 1):
            tmp[i] = A[i]

        i, j, k = s, m + 1, s
        while i <= m and j <= e:
            if tmp[i] <= tmp[j]:
                A[k] = tmp[i]
                k += 1
                i += 1
            else:
                A[k] = tmp[j]
                ans += j - k
                k += 1
                j += 1
        while i <= m:
            A[k] = tmp[i]
            k += 1
            i += 1
        while j <= e:
            A[k] = tmp[j]
            k += 1
            j += 1

    merge_sort(0, N - 1)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
