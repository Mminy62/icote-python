'''
- (N+1)개의 list를 갖는 2차원 list 생성
- 도시의 개수에 따라 count할 list 생성
- value가 K와 같은 index 추출
input
4 4 2 1
1 2
1 3
2 3
2 4
'''
from collections import deque
import sys
n, m, k, x = map(int, sys.stdin.readline().split())
adjList = [[] for _ in range(n+1)]
for _ in range(m):
    data = list(map(int,sys.stdin.readline().split()))
    adjList[data[0]].append(data[1])

queue = deque([x])
distance = [0] * (n + 1) #경로 list
visited = [False] * (n+1) #방문 처리를 위한 list
visited[x] = True #시작 지점 방문 처리
#BFS
while queue:
    x = queue.popleft()
    if adjList[x]:
        for v in adjList[x]:
            if not visited[v]:
                distance[v] = distance[x] + 1
                visited[v] = True
                queue.append(v)

answer = True
for i, v in enumerate(distance):
    if v == k:
        print(i)
        answer = False

if answer:
    print(-1)