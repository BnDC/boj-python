def solution():
    cnt, now = 0, 0
    while True:
        if visited[now]:
            return -1
        if now == k:
            return cnt
        visited[now] = True
        now = arr[now]
        cnt += 1


if __name__ == "__main__":
    n, k = map(int, input().rstrip().split())
    arr = [int(input()) for _ in range(n)]
    visited = [False for _ in range(n)]
    print(solution())
