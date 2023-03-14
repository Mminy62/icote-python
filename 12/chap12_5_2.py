'''

input
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

print(-1 % 4) -> 이걸로 direction 설정
t 초가 끝난 다음에 회전 한다는 뜻
이동 후에 회전
'''
from collections import deque
n = int(input())
apples = int(input())

matrix = [[0] * (n + 1) for _ in range(n + 1)]
# 사과 위치 설정 2
for _ in range(apples):
    x, y = map(int, input().split())
    matrix[x][y] = 2

rotates = deque([])
times = int(input())
for _ in range(times):
    a, b = input().split()
    b = -1 if b == 'L' else 1
    rotates.append((int(a), b))

# 뱀 몸은 1로
x, y = (1, 1)
d = 0
pre_d = d # before direction
# 동 남 서 북
# D -> d += 1, L -> d -= 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# time
t = 0
# while 뱀의 좌표
snake = deque([(1, 1)])
while snake:
    t += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 1 or nx >= n + 1 or ny < 1 or ny >= n + 1:
        break
    if matrix[nx][ny] == 1:
        break

    # 게임 진행되는 경우
        # 사과를 먹은 경우
    if matrix[nx][ny] == 2:
        matrix[nx][ny] = 1
        # 사과 안먹은 경우
    if matrix[nx][ny] == 0:
        matrix[nx][ny] = 1 # 머리 이동
        rx, ry = snake.popleft()
        matrix[rx][ry] = 0 # 이전 값 지우기
        # 시간 지나고 방향 전환
    if rotates and t == rotates[0][0]: # 방향 전환
        pre_d = d
        d = (d + rotates.popleft()[1]) % 4
    snake.append((nx, ny))
    x, y = nx, ny


print(t)
