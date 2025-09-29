"""
# 백준
# No. 16922
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    curr_que = set([1, 5, 10, 50])
    for _ in range(N - 1):
        next_que = set()
        for _ in range(len(curr_que)):
            c = curr_que.pop()
            for q in [1, 5, 10, 50]:
                next_que.add(c + q)
        curr_que = next_que
    ans = len(set(curr_que))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
