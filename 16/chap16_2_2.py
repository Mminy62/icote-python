'''
(풀음)
위부터 아래로 내려오니까
우린 아래에서 위로 가는건가?

input
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''

n = int(input())
graph = []
dp = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    dp.append([0] * (i + 1))

dp[0] = graph[0]

for i in range(1, n):
    for j in range(len(graph[i])):
        if j == 0:
            dp[i][j] = graph[i][j] + dp[i-1][j]
        elif j == len(graph[i])-1:
            dp[i][j] = graph[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = graph[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
