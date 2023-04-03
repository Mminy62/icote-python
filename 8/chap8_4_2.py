'''
(풀이참조)
효율적 화폐구성
https://wooono.tistory.com/521
input
2 15
2
3
output
5
'''

n, m = map(int, input().split())
units = []
for _ in range(n):
    units.append(int(input()))

dp = [10001] * (m + 1)
dp[0] = 0

k = 0


for i in range(units[0], m + 1): # m은 최대 10000 -> m*n -> 10 ** 6 100만 통과
    for k in units: # unit은 최대 100개
        if dp[i-k] != 10001:
            dp[i] = min(dp[i], dp[i-k] + 1)

print(dp)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])