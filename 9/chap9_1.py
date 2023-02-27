'''
풀이 참조
다익스트라로 풀려니까 헷갈리고, 플로이드 워셜이라는 것만 보고 풀음

input
4 2
1 3
2 4
3 4

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''
import sys
INF = int(10e9)
n, m = map(int, input().split())

# graph 초기화
graph = [[INF] * (n + 1) for i in range(n+1)]
# 같은 지점은 0으로
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 방향성이 없는 도로이므로

x, k = map(int, sys.stdin.readline().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)
