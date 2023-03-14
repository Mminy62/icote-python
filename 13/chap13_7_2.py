'''

이중배열 다 돌면 그제서야 인구 이동

이중배열을 돌면서 인구이동이 없을 때까지 아래 방법대로 반복한다.
check -> 방문 배열을 이중 배열 크기로 하나 만들고, 새로 확인할 때마다 방문 배열은 초기화 한다.
        cnt 변수
bfs -> 방문하지 않았고, 상하좌우에 걸쳐지는 나라인 경우 연합국가 좌표에 추가한다.
        return에 이제까지의 연합 국가 list
연합국가 계산 -> bfs로 받은 연합국가들의 목록을 뽑아
(연합 인구수(sum)/이루는 칸의 개수 (len)) 인구수 수정

다시 이중배열 check 함수 실행
만약에 모두가 방문했는데 bfs로 가지 않았다. bfs 의 return 인 연합국가 리스트가 비어있으면 종료.
INPUT
2 20 50
50 30
20 40
'''
from collections import deque
n, L, R = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def bfs(x, y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(x, y)])
    temp = [(x, y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if not visited[nx][ny]:
                gap = abs(matrix[x][y] - matrix[nx][ny])
                if L <= gap and gap <= R:
                    q.append((nx, ny))
                    temp.append((nx, ny))
                    visited[nx][ny] = True

    if len(temp) == 1:
        return []
    return temp

def check():
    units = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                unit = bfs(i, j, visited)
                if unit:
                    units.append(unit)

    return units

def calculate(units):
    for unit in units:
        people = 0
        for (ux, uy) in unit:
            people += matrix[ux][uy]

        people //= len(unit)
        for (ux, uy) in unit:
            matrix[ux][uy] = people

    return

# units에 아무 값이 없을때까지 check 반복
cnt = 0
while True:
    units = check()
    if units:
        cnt += 1
        calculate(units)
    else:
        break

print(cnt)



