"""
# 백준
# No. 1639
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    S = input()

    # Logic
    dp = [0] * len(S)
    dp[0] = int(S[0])
    for i in range(1, len(S)):
        dp[i] = dp[i - 1] + int(S[i])
    dp.append(0)  # dp[-1] = 0

    max_len = 0
    for s in range(len(S)):
        for e in range(s + max(max_len - 1, 1), len(S), 2):
            m = (s + e) // 2
            # left  = S[s:m+1],   dp[m] - dp[s-1]
            # right = S[m+1:e+1], dp[e] - dp[m]
            if dp[m] - dp[s - 1] == dp[e] - dp[m]:
                max_len = max(max_len, e - s + 1)

    # Output
    print(max_len)


if __name__ == "__main__":
    main()
