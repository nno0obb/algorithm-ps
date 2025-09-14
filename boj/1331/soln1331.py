"""
# 백준
# No. 1331
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    P = [input() for _ in range(36)]

    # Logic
    P.append(P[0])

    ans = "Valid"
    if len(set(P)) != 36:
        ans = "Invalid"

    if ans == "Valid":
        for i in range(36):
            p1, p2 = P[i], P[i + 1]
            px1, py1 = p1[0], p1[1]
            px2, py2 = p2[0], p2[1]
            pdx = abs(ord(px1) - ord(px2))
            pdy = abs(int(py1) - int(py2))
            if pdx == 1 and pdy == 2:
                continue
            elif pdx == 2 and pdy == 1:
                continue
            else:
                ans = "Invalid"
                break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
