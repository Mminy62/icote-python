'''
(풀음)
n x m 크기의 금광이 있습니다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.
input
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''

test_case = int(input())

dx = [-1, 0, 1]
for _ in range(test_case):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    graph = []
    for i in range(0, n * m, m):
        graph.append(temp[i : i + m])

    dp = [[0] * m for _ in range(n)]
    for r in range(n):
        dp[r][0] = graph[r][0]

    for j in range(1, m):
        for i in range(n):
            max_value = 0
            for k in range(3):
                x = dx[k] + i
                y = j - 1
                if x < 0 or x >= n:
                    continue
                if max_value < dp[x][y]:
                    max_value = dp[x][y]

            dp[i][j] = graph[i][j] + max_value

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)