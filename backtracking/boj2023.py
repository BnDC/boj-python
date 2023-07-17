import math
import sys


def solution():
    candidates = [1, 2, 3, 5, 7, 9]
    answer = []

    def dfs(now):
        if get_length(now) == n:
            answer.append(now)
            return

        for candidate in candidates:
            _next = now * 10 + candidate
            if check_prime(_next):
                dfs(_next)

    dfs(0)

    return answer


def check_prime(num):
    if num == 1: return False

    for i in range(2, math.ceil(num ** 1 / 2)):
        if num % i == 0:
            return False
    return True


def get_length(num):
    result = 0
    while num != 0:
        num //= 10
        result += 1
    return result


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    ans = solution()
    for a in ans:
        print(a)
