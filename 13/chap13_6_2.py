'''
INPUT
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
'''

# 선생님과 빈칸의 좌표 담기
from collections import deque
from itertools import combinations
n = int(input())

matrix = []
for _ in range(n):
    matrix.append(input().split())

teacher = []
empty = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'T':
            teacher.append((i, j))
        if matrix[i][j] == 'X':
            empty.append((i, j))

def check(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        tx, ty = x, y

        while True: # tx ty, 알아서 마주치면 break
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if matrix[nx][ny] == 'O':
                break
            if matrix[nx][ny] == 'S':
                return False

            #empty 아니면 T
            tx, ty = nx, ny

    return True

wall_list = list(combinations(empty, 3))

for walls in wall_list:
    flag = 0
    for i in range(3): # 벽 설치
        wx, wy = walls[i]
        matrix[wx][wy] = 'O'

    # 선생님 감시 방향 확인
    for tx, ty in teacher:
        if not check(tx, ty):# 학생 마주침
            flag = 1
            break
        else:# 학생 안마주침
            continue
    # 마주쳤는지 유무
    if flag == 0:
        print("YES")
        break
    else:# 마주쳐서 새로 설치
        for i in range(3):  # 벽 허물기
            wx, wy = walls[i]
            matrix[wx][wy] = 'X'

if flag == 1:
    print("NO")




