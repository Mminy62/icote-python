import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

s, x, y = map(int, input().split())
# 바이러스별 좌표 모음
graph = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            heapq.heappush(graph, (matrix[i][j], (i, j)))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(s):
    temp = []
    while graph:
        virus, (vx, vy) = heapq.heappop(graph)

        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] != 0:
                continue
            if matrix[nx][ny] == 0:
                heapq.heappush(temp, (virus, (nx, ny)))
                matrix[nx][ny] = virus

    graph = temp[:]

print(matrix[x-1][y-1])