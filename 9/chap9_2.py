'''
input
3 2 1
1 2 4
1 3 2

시간을 다익스트라의 경로라고 생각하고 똑같이 구현하되,
많이 퍼지는게 최단 시간보다 우선 순위인줄 알고, k를 거치는 노드가 있으면 무조건 추가하였다.
문제에서 C가 응급상황이고, 최대한 많이 보내는 것이기 때문에, 최단 시간일때 얼마나 퍼지냐가 중요한 것 같다.
'''
import heapq
INF = int(10e9)
n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
time = [INF] * (n + 1)  #최단 거리 테이블
visited = [False] * (n + 1)

for i in range(m):
    x, y, t = map(int, input().split())
    graph[x].append((y, t))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리를 시간으로 생각? ## 일단 시간을기준으로 하지만 다 선형탐색
    time[start] = 0

    while q:
        ti, now = heapq.heappop(q)
        if visited[now]:  # 2 가 만약에 나중에 나올 수도 있는데...(2, 3) (3, 4) 다 처리 완료 -> 2와 연결된 (3, 4) (4, 5)
            continue

        for j in graph[now]: # 인접한 노드가 있는 경우, 시간도 있음
            # 현재 노드까지의 시간 j는 graph에 있는 node (인덱스, 시간)
            cost = ti + j[1]
            time[j[0]] = cost # 하나를 더 거쳐가면 시간이 오래 걸려도 상관 없음

            heapq.heappush(q, (cost, j[0]))

            # #### 어차피 방향성이 있으니까 방문했던 노드는 다시 재방문 X
            visited[now] = True

dijkstra(start)

city = list(filter(lambda x: x != INF, time))
print(len(city) - 1, max(city))