"""
# 백준
# No. 1371
# Python 3.11.9
# by "nno0obb"
"""

import re
from collections import Counter


def main():
    # Input
    text = ""
    while True:
        try:
            text += input()
        except EOFError:
            break

    # Logic
    counter = Counter(re.sub(r"[^a-z]", "", text))
    most_common_freq = counter.most_common(1)[0][1]
    most_common_chars = [char for char, freq in counter.items() if freq == most_common_freq]

    # Output
    print("".join(sorted(most_common_chars)))


if __name__ == "__main__":
    main()
