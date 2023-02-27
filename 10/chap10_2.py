'''
n 개의 마을 노드 m개의 길
길마다 간선 비용 있음
2개의 분리된 마을로 만들 것 -> join 으로  부모 2개
각 분리된 마을 안에는 최소 신장 트리로 만들 것 -> 크루스탈 2번

풀이 참조
-> 부모가 하나일 수도 있다는 생각을 못함
-> 크루스칼로 최소 신장 트리를 구한 뒤 가장 큰 간선 비용을 지우면 됨.

input
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''

import sys

input = sys.stdin.readline

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

n, m = map(int, input().split())

parent = [0] * (n + 1)
edges = []

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0
max_cost = 0

for edge in edges:
    cost, a, b = edge
    # 사이클이 안만들어 질 때 집합으로 합치는 것이 크루스칼 # 정렬 후에 하는 반복문으로 알아서 최소 간선으로 지정됨.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        # if cost > max_cost:
        #     max_cost = cost
        ## 정렬 후의 간선이기 때문에, 마지막 cost 가 가장 큰 값.
        max_cost = cost


print(result - max_cost)



