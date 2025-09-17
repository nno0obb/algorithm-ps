"""
# 백준
# No. 11059
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    S = input()

    # Logic
    dp = [0] * (len(S) + 1)
    dp[0] = 0  # S[0:0)
    dp[1] = 0  # S[0:1)
    for i in range(1, len(S) + 1):
        dp[i] = dp[i - 1] + int(S[i - 1])

    max_len = 2
    for s in range(len(S)):
        for e in range(s + max_len, len(S) + 1, 2):
            m = (s + e) // 2
            # L, R = S[s:m], S[m:e]
            if dp[m] - dp[s] == dp[e] - dp[m]:
                max_len = max(max_len, e - s)

    # Output
    print(max_len)


if __name__ == "__main__":
    main()
