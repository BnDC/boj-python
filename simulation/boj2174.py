import sys

directions = {"E": 0, "N": 1, "W": 2, "S": 3}
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def solution():
    for idx, order, cnt in orders:
        r, c, d = robots[idx]
        if order == "L":
            d = (d + cnt) % 4
            robots[idx] = [r, c, d]
        elif order == "R":
            d = (d + 3 * cnt) % 4
            robots[idx] = [r, c, d]
        elif order == "F":
            for _ in range(cnt):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 1 or nr > row_length or nc < 1 or nc > col_length:
                    return "Robot {} crashes into the wall".format(idx)
                if graph[nr][nc] != 0:
                    return "Robot {} crashes into robot {}".format(idx, graph[nr][nc])
                graph[r][c] = 0
                graph[nr][nc] = idx
                r, c = nr, nc
                robots[idx] = [nr, nc, d]
    return "OK"


if __name__ == "__main__":
    input = sys.stdin.readline
    col_length, row_length = map(int, input().rstrip().split())
    n, m = map(int, input().rstrip().split())

    graph = [[0] * (col_length + 1) for _ in range(row_length + 1)]

    robots = [(-1, -1, -1)]
    for i in range(1, n + 1):
        start_x, start_y, direction = input().rstrip().split()
        input_robot = [int(start_y), int(start_x), directions[direction]]
        graph[input_robot[0]][input_robot[1]] = i
        robots.append(input_robot)

    orders = []
    for _ in range(m):
        input_robot, input_order, input_cnt = input().rstrip().split()
        orders.append((int(input_robot), input_order, int(input_cnt)))

    print(solution())
