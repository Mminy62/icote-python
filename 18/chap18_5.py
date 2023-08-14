'''
1
5
5 4 3 2 1
2
2 4
3 4
input
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
'''
from collections import deque

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    last = list(map(int, input().split()))
    # graph, indegree 초기화
    for i in range(1, n + 1):
        #graph[last[i-1]].append(last[i])
        graph[last[i-1]].append(last[i:])
        print(last, indegree)
        indegree[last[i]] += 1

    #change current year
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        b_index = last.index(b)
        if a not in last[b_index:]:
            print("IMPOSSIBLE")
        else:
            if a in graph[b]:
                graph[b].remove(a)
                indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1

def topology():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology()

