import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution():
    visited = [[False] * 3 for _ in range(3)]
    q = deque()
    total = 0
    result = []
    for i in range(3):
        for j in range(3):
            if visited[i][j]: continue
            if arr[i][j] != "O": continue
            q.append((i, j))
            total += 1
            cnt = 0
            while q:
                x, y = q.popleft()
                if visited[x][y]: continue
                cnt += 1
                visited[x][y] = True

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= 3 or ny < 0 or ny >= 3: continue
                    if arr[nx][ny] != "O": continue
                    q.append((nx, ny))
            result.append(cnt)
    result.sort()
    return [total] + result


if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        arr = [input().rstrip() for i in range(3)]
        answer = list(map(int, input().rstrip().split()))
        if solution() == answer:
            print(1)
        else:
            print(0)
