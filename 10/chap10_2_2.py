def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    flag = False
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        flag = True

    return flag





n, m = map(int, input().split())
parent = [0]
for i in range(1, n + 1):
    parent.append(i)

graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()
result = []
for c, a, b in graph:
    if union_parent(parent, a, b):
        result.append(c)
print(result)

print(sum(result) - max(result))
