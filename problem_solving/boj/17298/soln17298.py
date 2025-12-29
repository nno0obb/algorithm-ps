"""
# 백준
# No. 17298
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    stack = []
    NGE = [-1] * N
    for idx, num in enumerate(A):
        while stack and stack[-1][1] < num:
            _idx, _num = stack.pop()
            NGE[_idx] = num
        stack.append((idx, num))

    # Output
    print(*NGE)


if __name__ == "__main__":
    main()
