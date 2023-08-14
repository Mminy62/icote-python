'''
#어차피 n개의 노드에 n-1개의 간선만 연결하면 모든 노드는 다 연결된다.
# 그럼 cost중에서 가장 작은 cost만 연결하면 되는데, x 좌표끼리, y, z 좌표의 각각의 값 중 최소값이기 때문에, n개의 x, y, z 좌표들을 수집하여 각각을 sorting해준 후 값을 넣으면 된다.
for i in range(n):
    xa, ya, za = graph[i]
    for j in range(i + 1, n):
        xb, yb, zb = graph[j]

        cost = min(abs(xa-xb), abs(ya-yb), abs(za-zb))
        edges.append((cost, i, j))
이 코드 대로 하니까 edges의 경우의 수가 많아 메모리 초과가 났다. 그도 그럴 것이 n이 10만이라 O(N^2)이 10억이다^,,



input
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''
import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
edges = []
coorx = []
coory = []
coorz = []

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    x, y, z = map(int, input().split())
    coorx.append((x, i))
    coory.append((y, i))
    coorz.append((z, i))

coorx.sort()
coory.sort()
coorz.sort()

result = 0
for i in range(1, n):
    edges.append((abs(coorx[i-1][0] - coorx[i][0]), coorx[i-1][1], coorx[i][1]))
    edges.append((abs(coory[i - 1][0] - coory[i][0]), coory[i - 1][1], coory[i][1]))
    edges.append((abs(coorz[i - 1][0] - coorz[i][0]), coorz[i - 1][1], coorz[i][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
