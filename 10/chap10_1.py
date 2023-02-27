'''
학교 학생들에게 0번부터 N번까지의 번호를 부여했다.
팀 합치기 union, 같은 팀 여부 확인find 연산 -> 같은 루트노드를 갖고 있는지 확인
=> 서로소 집합 알고리즘 (union-find)

input
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n + 1)
result = []

# 부모 테이블을 자기 자신으로 초기화
for i in range(n + 1):
    parent[i] = i

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



for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")


print(result)