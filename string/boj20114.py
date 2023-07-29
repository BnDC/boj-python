import sys


def solution():
    answer = ["?" for _ in range(n)]
    for i in range(0, n * w - w + 1, w):
        for k in range(h):
            for j in range(w):
                if arr[k][i + j] != "?":
                    answer[i // w] = arr[k][i + j]
    return ''.join(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, h, w = map(int, input().rstrip().split())
    arr = [input().rstrip() for _ in range(h)]
    print(solution())
