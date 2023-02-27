'''
풀이 참조
각 노드별로 count 하는 아이디어는 맞는데 플로이드로 풀어야하는지 몰랐음.
(다익스트라, 플로이드 개념이 좀 헷갈리는듯)

input
6 6
1 5
3 4
4 2
4 6
5 2
5 4

'''
import sys
INF = int(10e9)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

# input init
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


# floyd
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# graph 를 통해서 1번 행은 1번 학생이고, 1행에 INF가 아닌 열은 해당 열의 번호의 학생과 1번 학생이 연결되어 있다는 뜻이다.
result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    if count == n:
        result += 1

print(result)