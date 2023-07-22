import sys

BASE = ord("A")


def solution():
    for i in range(35):
        now_r, now_c = get_coordinate(moves[i][0], moves[i][1])
        next_r, next_c = get_coordinate(moves[i + 1][0], moves[i + 1][1])
        if board[now_r][now_c] != 0:
            return "Invalid"
        board[now_r][now_c] = i + 1

        diff = (abs(next_r - now_r), abs(next_c - now_c))
        if diff != (2, 1) and diff != (1, 2):
            return "Invalid"

    first_r, first_c, = get_coordinate(moves[0][0], moves[0][1])
    last_r, last_c = get_coordinate(moves[-1][0], moves[-1][1])

    diff = (abs(first_r - last_r), abs(first_c - last_c))
    if diff != (2, 1) and diff != (1, 2):
        return "Invalid"
    if board[last_r][last_c] != 0:
        return "Invalid"
    return "Valid"


def get_coordinate(str_x, str_y):
    return 6 - int(str_y), ord(str_x) - BASE


if __name__ == "__main__":
    input = sys.stdin.readline

    board = [[0] * 6 for _ in range(6)]
    moves = [input().rstrip() for _ in range(36)]
    print(solution())
