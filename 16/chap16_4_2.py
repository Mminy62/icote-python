'''
(풀이참조)
LIS

input
7
15 11 4 8 5 2 4

n <= 2000
2000 * 2000 -> 000000- > 4백만 가능
# 15 11 8 5 4 4 2
# 15 11 4 8 5 2 4 -> 가장 오름차순 길이가 긴 걸 빼기

'''

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

arr.reverse()

for i in range(1, n):
    for j in range(0, i):
        if arr[j] <= arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))


