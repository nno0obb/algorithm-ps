"""
# 백준
# No. 24051 
# Python 3.11.9 (PyPy3)
# by "nno0obb"
"""

# Global Variables
K = 0


def insertion_sort(A: list[int]):
    global K

    cnt = 0
    for i in range(1, len(A)):
        loc = i - 1
        new_item = A[i]
        while 0 <= loc and new_item < A[loc]:
            A[loc + 1] = A[loc]
            cnt += 1
            if cnt == K:
                return A[loc + 1]
            elif cnt > K:
                return -1
            loc -= 1
        if (loc + 1) != i:
            A[loc + 1] = new_item
            cnt += 1
            if cnt == K:
                return A[loc + 1]
            elif cnt > K:
                return -1
    return -1


def main():
    global K

    # Input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    ans = insertion_sort(A)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
