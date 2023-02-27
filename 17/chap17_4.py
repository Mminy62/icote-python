'''
다익스트라
input
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(10e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1
distance[start] = 0
q = []

heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    # 현재 노드에서 가장 작은 것 뽑아야지 ->  그게 dist, now
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

for i in range(n + 1):
    if distance[i] == INF:
        distance[i] = -1

max_value = max(distance)
max_pos = distance.index(max_value)
max_dist = distance[max_pos]
max_num = len(list(filter(lambda x: x == max_value, distance)))

print(max_pos, max_dist, max_num)


