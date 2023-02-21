'''
풀이 참조

DP의 점화식을 세울 땐, 항상 탐색할 항의 기준을 정하고, 그 이전 항과의 관계를 생각해야한다.
구하려는 항: 마지막 m열에 도착했을 때, 가장 큰 금광 채굴 양
이전 항: 이전 열에서의 선택지 -> 이전 열의 선택지까지의 최대값 이므로 결국 바로 n-1항만 살펴보면 되는 점화식을 세울 수 있음.
그러므로 bottom-up 방식
input
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

1
3 4
1 3 3 2 2 1 4 1 0 6 4 7
'''

case_num = int(input())
n, m = map(int, input().split())

array = []
temp = list(map(int, input().split()))

#input array 생성
for i in range(0, n * m, m):
    array.append(temp[i: i + m])

print(array)

result = [[0] * m for _ in range(n)]

for i in range(n):
    result[i][0] = array[i][0]

for j in range(m):
    for i in range(n):
        if i == 0:
            top = -1
            down = array[i][j] + result[i+1][j-1]
        elif i == n-1:
            top = array[i][j] + result[i-1][j - 1]
            down = -1

        elif i == n-1 and i == 0:
            top, down = -1, -1
        else:
            top = array[i][j] + result[i - 1][j - 1]
            down = array[i][j] + result[i+1][j-1]

        middle = array[i][j] + result[i][j - 1]

        result[i][j] = max(result[i][j], top, middle, down)

print(result)