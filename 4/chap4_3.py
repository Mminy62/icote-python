'''
게임 캐릭터는 n * m 크기의 직사각형 맵에서 움직인다.
각각의 칸은 육지 / 바다
캐릭터는 동서남북 중 한 곳을 바라본다. (방향 O)
A, B -> X, Y
캐릭터는 육지만 갈 수 있음
1. 캐릭터의 방향은 현재 기준으로 왼쪽부터 시작한다. 현재가 북이면 서부터
2. 회전 방향에 아직 가보지 못한 육지가 존재하면 회전 후 한칸 이동. 만약 가보지 않은 칸이 없다면 회전만 수행하고 1단계로 돌아간다.
3. 만약 네방향 다 이미 가본 칸이거나 바다인 경우,
바라보는 방향을 유지한 채 한칸 뒤로 가고 1단계로 돌아간다. 단 이때 뒤쪽이 바다인 경우 뒤로도 갈 수 없으므로 움직임을 멈춘다.

방향 경험해보는 count 변수 필요 -> 그냥 다 돌면 -> 해당 방향에서 뒤로 보내기
가볼 수 있는 칸이 있으면 break
output 캐릭터가 방문한 칸의 수를 출력하는 프로그램
Input
# n, m
# (1, 1)에서 북쪽을 바라보고 있는 캐릭터
# 북 동 남 서 -> 0 1 2 3
# 육지 - 0, 바다 - 1
# 캐릭
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

1. 인풋값 그래프로 받고
2. 해당 nx, ny 가 방향대로 (x + 1) % 4 해서 방향 회전 후 앞으로 나아간 값 다 해당이 안되면 해당 방향만큼 뒤로# 원래 처음 방향에서 뒤로 한칸 - 붙여서 보내기
'''
from collections import deque
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

if direction == 1 or direction == 3:
    direction = (direction + 2) % 4

graph = []
q = deque([(x, y)])

for _ in range(n):
    graph.append(list(map(int, input().split())))

graph[x][y] = 1
cnt = 1
#북서남동 순
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
#direction += 1 의 방향부터

while q:
    x, y = q.popleft()
    direction += 1

    for i in range(4):
        nx = x + dx[(direction + i) % 4]
        ny = y + dy[(direction + i) % 4]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            continue
        if graph[nx][ny] == 0:
            q.append((nx, ny))
            graph[nx][ny] = 1
            cnt += 1
            break

print(cnt)
