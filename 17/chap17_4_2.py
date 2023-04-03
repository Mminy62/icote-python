'''
다익스트라, 1번째 지점이 시작
output
max(distance), max distance에 해당하는 index를 담고 거기서 제일 작은 번호를 출력, 같은 거리의 갯수 찾기(본인제외)
output
헛간 번호, 헛간 거리, 같은 거리의 헛간 개수

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
    graph[a].append((b, 1)) # a -> b 거리 1
    graph[b].append((a, 1)) # 양방향 이므로 b -> a 거리 1

q = []
distance[1] = 0
heapq.heappush(q, (0, 1)) # 거리 0, 시작 지점 1

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

max_dist = max(distance[1:])
result = []
for i, v in enumerate(distance):
    if v == max_dist:
        result.append(i)

print(min(result), max_dist, len(result))

