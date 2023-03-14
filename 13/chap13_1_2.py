'''

X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
output
d에서 조건 맞는 인덱스 출력
없으면 -1
input
4 4 2 1
1 2
1 3
2 3
2 4
'''

n, m, k, start = map(int, input().split())
d = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(start):
    v = d[start]
    for i in graph[start]:
        if d[i] == 0 or d[i] > v + 1:
            d[i] = v + 1
            if graph[i]: # 값이 있다면 더 깊이
                dfs(i)
        else:
            return 0

    return 0

dfs(start)
answer = []
for i, v in enumerate(d):
    if v == k:
        answer.append(i)

if len(answer):
    for i in range(len(answer)):
        print(answer[i])
else:
    print(-1)
