'''
n, m
m개의 연결
x, k

1 -> K -> X

input
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력
3
'''
import sys
input = sys.stdin.readline
INF = int(10e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for c in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][c] + graph[c][j])


result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)


