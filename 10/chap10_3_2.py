'''
위상 정렬
(풀이 참조)
input
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

'''
from collections import deque
from copy import deepcopy
n = int(input())
indegree = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

#input값 받기
for i in range(1, n + 1):
    temp = list(map(int, input().split()))[:-1]
    time[i] = temp[0]

    for x in temp[1:]:
        graph[x].append(i)
        indegree[i] += 1

print(indegree)

def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    result = deepcopy(time)
    # 1 넣고
    while q:
        now = q.popleft()
        for b in graph[now]:# 현재 노드랑 이어져 있는걸 찾는거야 현재노드가 출발지점, 이어져 있는 진입차수 줄여주기
            indegree[b] -= 1
            result[b] = max(result[b], result[now] + time[b])
            if indegree[b] == 0:
                q.append(b)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()


