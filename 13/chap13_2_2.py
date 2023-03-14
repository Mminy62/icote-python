'''
INPUT

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

4 4
2 2 0 0
2 0 0 0
0 0 0 0
0 0 0 0
'''
from itertools import combinations
from collections import deque
from copy import deepcopy
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

home = []
virus = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            home.append((i, j))
        if graph[i][j] == 2:
            virus.append((i, j))

wall_list = list(combinations(home, 3))

q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

for walls in wall_list:
    #temp_graph = graph[:]
    temp_graph = deepcopy(graph)
    for i in range(3): # 조합의 결과로 임의로 벽 설치
        wx, wy = walls[i]
        temp_graph[wx][wy] = 1

    for vx, vy in virus:
        q = deque([(vx, vy)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if temp_graph[nx][ny] >= 1:
                    continue
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    q.append((nx, ny))

    #temp_graph 에서 안전영역 찾기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                cnt += 1

    if answer < cnt:
        answer = cnt

print(answer)