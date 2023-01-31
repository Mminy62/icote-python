'''
input
4 5
00110
00011
11111
00000
'''

## main
#input 값 넣기
n, m = map(int, input().split())
matrix = []
count = 0


for _ in range(n):
    matrix.append(list(map(int, input())))

## DFS 로 구현한 코드
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if matrix[x][y] == 0:
        # 해당 노드 방문 처리
        matrix[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    # matrix[x][y] == 1 # 벽이거나 방문했던 곳이면 False 반환
    return False


result = 0
## main
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

# ## BFS 로 구현한 코드
from collections import deque

def bfs(matrix, start):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            elif matrix[nx][ny] == 1:
                continue

            elif matrix[nx][ny] == 0:
                queue.append((nx, ny))
                matrix[nx][ny] = 1

    return matrix

####main
n, m = map(int, input().split())
matrix = []

for _ in range(n):
    temp = []
    s = input()
    for i in range(m):
        temp.append(int(s[i]))
    matrix.append(temp)

result = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            matrix = bfs(matrix, (i, j))
            result += 1

print(result)