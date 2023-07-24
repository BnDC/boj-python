import sys


def find(p, a):
    if p[a] != a:
        p[a] = find(p, p[a])
    return p[a]


def union(p, a, b):
    pa = find(p, a)
    pb = find(p, b)

    if pa < pb:
        p[pb] = pa
    else:
        p[pa] = pb


def solution():
    t = int(input())
    for i in range(t):
        print("Scenario {}:".format(i + 1))
        n = int(input())
        k = int(input())
        parent = [e for e in range(n)]
        for _ in range(k):
            a, b = map(int, input().rstrip().split())
            union(parent, a, b)

        m = int(input())
        for _ in range(m):
            u, v = map(int, input().rstrip().split())
            if find(parent, u) == find(parent, v):
                print("1")
            else:
                print("0")
        print()


if __name__ == "__main__":
    input = sys.stdin.readline
    solution()
