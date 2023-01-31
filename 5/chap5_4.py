'''
미로 찾기는 BFS
묶음 세기는 DFS
input
5 6
101010
111111
000001
111111
111111

상하좌우 둘러보고 1이면 이동, 큐에 삽입
1발견 할때마다 count + 1
'''
from collections import deque

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input())))

queue = deque([(0, 0)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if matrix[nx][ny] == 0:
            continue

        if matrix[nx][ny] == 1:
            queue.append((nx, ny))
            matrix[nx][ny] = matrix[x][y] + 1

    #matrix[x][y] = 0



for i in range(n):
    print(matrix[i])
print(matrix[n-1][m-1]+1)
