'''
5:08 - 7:21
(2시간)
- 먼저 묶음을 만들고 연합국을 생성한다.

- visited 배열을 만들어 bfs로 방문한 흔적을 남긴다.
방문하지 않은 지점에서 bfs를 시작하고
주변 국을 탐색하여 해당하는 나라의 index를 추가한 묶음 배열을 생성한다.
(bfs의 return 값은 묶음 배열)

- bfs 구현
bfs는 현재와 주변 나라의 값 차이가 L이상 R이하인 것을 더해주면 된다.
(bfs의 시작지점을 묶음 배열의 초기값으로 준 상태이므로,
주변에 해당하는 나라가 없는 경우 return 값을 다르게 주어야한다.)

- bfs의 인구 이동 시작
전체 인구 이동이 끝났으면 -> visited 0으로 초기화, 날짜 count + 1

다시 반복

#후기:
처음에 dfs, 
처음에 문제를 제대로 안읽고 나라별 인구수가 L이상 R이하이면 모두 해당하는 것인줄 알아,
오류를 찾는데 시간을 허비

input
2 20 50
50 30
20 40
'''
from collections import deque
import math

N, L, R = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]


def bfs(start):  # return units index list
    queue = deque([start])

    index_list = [start]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while (queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 1:
                continue

            diff = abs(matrix[x][y]-matrix[nx][ny])
            if diff >= L and diff <= R:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                index_list.append((nx, ny))

    if len(index_list) == 1: #차이나는 주변국이 없는 경우
        return 0

    return index_list

def search():
    count = 0
    flag = 0
    global visited

    while (flag == 0):
        # bfs가 끝났음에도 uindx(차이 있는 주변국이 없으면)가 비어있으면 count 종료
        # bfs 로 주변국 탐색 시작
        uindex = []

        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    continue
                else:
                    visited[i][j] = 1
                    temp = bfs((i, j))
                    if temp != 0:
                        uindex.append(temp)
        if not uindex:
            flag = 1
            return count

        # 인구 이동 시작
        for countries in uindex:
            peos = 0
            for index in countries:
                x, y = index
                peos += matrix[x][y]

            peos = math.floor(peos // len(countries))
            for x, y in countries:
                matrix[x][y] = peos

        # 인구 이동 끝
        count += 1

        # 방문 초기화
        visited = [[0] * N for _ in range(N)]

print(search())

