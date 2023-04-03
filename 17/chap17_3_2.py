'''
화성탐사

start = [0][0]인 다익스트라
1
3
5 5 4
3 9 1
3 2 7
'''
import heapq
INF = int(10e9)

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    graph = []
    distance = [[INF] * n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # dijkstra
    q = []
    heapq.heappush(q, (graph[0][0], (0, 0)))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        dist, (x, y) = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        # 인접한 4 곳이 연결된 것
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

    print(distance[n-1][n-1])