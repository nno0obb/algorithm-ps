"""
# 백준
# No. 2739 
# Python 3.11.9
# by "nno0obb"
"""

from string import Template


def main():
    # Input
    N = int(input())

    # Logic
    row_format = Template("$N * $i = $result")
    ans = "\n".join(row_format.substitute(N=N, i=i, result=N * i) for i in range(1, 10))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
