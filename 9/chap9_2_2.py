'''

c에서 모든 지점으로 퍼지는

input
3 2 1
1 2 4
1 3 2
output
2 4

'''
import heapq
INF = int(10e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

q = []
heapq.heappush(q, (0, c)) # start지점인 c에서
distance[c] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: # 현재 노드가 INF가 아닌 이미 처리된 노드라면 pass
        continue
    for i in graph[now]:
        cost = dist + i[1]
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt = 0
for i in range(0, n + 1):
    if distance[i] == INF:
        distance[i] = 0
    else:
        cnt += 1

print(cnt - 1, max(distance)) # c 빼야하므로 cnt - 1
