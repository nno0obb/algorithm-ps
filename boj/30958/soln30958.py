"""
# 백준
# No. 30958
# Python 3.11.9
# by "nno0obb"
"""

import re
from collections import Counter


def main():
    # Input
    N = int(input())
    logo_song = input()

    # Logic
    logo_song = re.sub(r"[^a-z]", "", logo_song)
    freq = Counter(logo_song).most_common(1)[0][1]

    # Output
    print(freq)


if __name__ == "__main__":
    main()
