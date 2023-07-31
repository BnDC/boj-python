import sys


def dfs(prefix: str, cnt: int):
    print(prefix + q)
    if cnt == 0:
        print(prefix + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(prefix + last_line)
        return

    print(prefix + first_line)
    print(prefix + second_line)
    print(prefix + third_line)
    dfs(prefix + "____", cnt - 1)
    print(prefix + last_line)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    q = "\"재귀함수가 뭔가요?\""
    first_line = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
    second_line = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    third_line = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

    last_line = "라고 답변하였지."

    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    dfs("", n)
