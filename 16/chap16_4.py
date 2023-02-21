'''
풀이 참조
전형적인 DP, LIS 유형 문제(가장 긴 부분 수열을 구하는 문제)

자신보다 왼쪽에 작은 수가 얼마나 많이 있는지를 확인하는 문제.
이게 왜 dp일까, dp table에 자신 보다 왼쪽에 있는 수 중에 작은 부분 배열의 최대 길이를 넣는다.
dp Table을 쓰기 때문에 왼쪽 부분의 부분 배열을 매번 찾는 반복문을 줄여준다.

input
7
15 11 4 8 5 2 4
'''

n = int(input())
cnt = 0

soldiers = list(map(int, input().split()))
soldiers.reverse()
dp = [1] * n #부분 수열의 명 수 표시 #해당 인덱스까지의 연속된 숫자

for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))