"""
# 백준
# No. 16113
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S = input()

    # Logic
    m, n = 5, N // 5
    B = []
    for i in range(5):
        B.append(S[i * n : (i + 1) * n] + "..")

    ans, x = [], 0
    while x < n:
        if B[0][x] == "#":
            col_1 = "".join([B[y][x] for y in range(m)])
            x += 1
            col_2 = "".join([B[y][x] for y in range(m)])
            x += 1
            col_3 = "".join([B[y][x] for y in range(m)])

            match (col_1, col_2):
                case ("#####", "#...#"):
                    ans.append(0)
                case ("#####", "....."):
                    ans.append(1)
                    x -= 2
                case ("#.###", "#.#.#"):
                    ans.append(2)
                case ("#.#.#", "#.#.#"):
                    ans.append(3)
                case ("###..", "..#.."):
                    ans.append(4)
                case ("###.#", "#.#.#"):
                    match (col_3):
                        case "#.###":
                            ans.append(5)
                        case "#####":
                            ans.append(9)
                        case _:
                            raise RuntimeError()
                case ("#####", "#.#.#"):
                    match (col_3):
                        case "#.###":
                            ans.append(6)
                        case "#####":
                            ans.append(8)
                        case _:
                            raise RuntimeError()
                case ("#....", "#...."):
                    ans.append(7)
                case _:
                    raise RuntimeError()
        x += 1

    # Output
    print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
