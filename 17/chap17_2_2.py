'''
(풀이 참조)
n, m
a < b 점수 라는 거

a -> b로의 단방향이므로, 플로이드 워셜을 사용해 점수 비교를 하는 것은 알았으나,
b -> a를 생각하지 못함.

문제 풀이
a -> b는 a < b 점수라는 의미이므로, 반대로 a -> b가 안되는 부분이 b -> a로 닿는 지점이 생기면, b < a 라는 의미로
성적 비교가 a, b의 성적 비교가 가능해진다.
그러므로 1개의 행에서 n개의 열 모두에 INF(초기값)이 아닌 값이 존재한다면
성적 비교가 가능하다는 것이므로 그 값을 count 하면 된다.

output
1
# 정확히 순위를 알 수 있는 학생
input
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
INF = int(10e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
result = 0
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

#Floyd
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)


