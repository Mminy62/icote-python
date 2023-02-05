'''
1. 2차원 배열 돌면서 0, 1, 2 중 0, 2에 대해서 index 리스트를 따로 만들어 놓는다.
2. 빈칸인 0 리스트의 index 로 조합 3을 만들고
그 조합을 가장 겉에 반복문에 배치시킨다.
3. 조합 리스트를 돌때마다 바이러스가 퍼져야하므로, 2인 바이러스 리스트를 시작점으로 bfs를 돌린다. matrix로 반환
4. matrix의 0의 갯수중 가장 최대인 것을 찾아라. count(0)
'''
from collections import deque
from itertools import combinations
from copy import deepcopy


# 3 bfs
def bfs(modi, virus):
    for start in virus:
        queue = deque([start])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if modi[nx][ny] > 0:
                    continue
                if modi[nx][ny] == 0:
                    modi[nx][ny] = 2
                    queue.append((nx, ny))

    return modi


# 1
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

house = deque([])
virus = deque([])

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            house.append((i, j))
        if matrix[i][j] == 2:
            virus.append((i, j))

# 2
walist = list(combinations(house, 3))
result = 0

for walls in walist:
    temp = deepcopy(matrix)

    for i in range(3):
        x, y = walls[i]
        temp[x][y] = 1

    temp = bfs(temp, virus)

    cnt = 0
    for i in range(n):
        cnt += temp[i].count(0)
    if result < cnt:
        result = cnt

print(result)

