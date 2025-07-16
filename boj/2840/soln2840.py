"""
# 백준
# No. 2840 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())
    SC = []
    for _ in range(K):
        s, c = input().split()
        SC.append([int(s), c])

    # Logic
    wheel = ["?"] * N
    idx = 0
    for s, c in SC:
        idx += s
        idx %= N
        if wheel[idx] == "?":
            wheel[idx] = c
        elif wheel[idx] != c:
            wheel = ["!"]
            break

    if wheel != ["!"]:
        alphabets = list(filter(lambda x: x != "?", wheel))
        if len(set(alphabets)) != len(alphabets):
            wheel = ["!"]

    if wheel != ["!"]:
        wheel = wheel[idx::-1] + wheel[:idx:-1]
    wheel = "".join(wheel)

    # Output
    print(wheel)


if __name__ == "__main__":
    main()
