'''
INPUT
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''
from itertools import combinations
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

house = []
store = [] # (x, y), cnt
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            store.append((i, j))

store = list(combinations(store, m))

answer = []

for store_list in store:
    result = 0
    for hx, hy in house:
        d = 51
        for sx, sy in store_list:
            temp = abs(hx-sx) + abs(hy-sy)
            if temp < d:
                d = temp
        result += d
    answer.append(result)


print(min(answer))
