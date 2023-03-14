'''
INPUT
4 5
00110
00011
11111
00000
'''
from collections import deque
n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(i, j):

    q = deque([(i, j)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
    return 0

cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            cnt += 1
            graph[i][j] = 1

print(cnt)