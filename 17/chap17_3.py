'''
bfs, 최단 경로 합쳐서 생각
특정 지점에서 특정 지점까지의 최단 거리 -> 다익스트라
input
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
import heapq
INF = int(10e9)
test_num = int(input())

for _ in range(test_num):
    n = int(input())

    # 그래프 초기화
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    # bfs 느낌으로 인접한 노드 중 짧은 것 찾기
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0)) # dist, index

    while q:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        dist, x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if distance[nx][ny] < dist: #이미 처리된 노드인 경우 노드 자체를 무시하면 되니까 for문 위에 if distance[x][y] < dist 해도된다.
                continue

            cost = dist + graph[nx][ny]
            #print(cost)
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
                #print(cost, (nx, ny))

    print(distance[n-1][n-1])