'''
풀이참조

2, 3, 5 로 나누어 떨어지고 다른 수로 나누어 떨어지면 합성수가 아닌 것으로 생각할까 했지만,
너무 비효율적이다. n**2이 나옴

'''

n = int(input())

dp = [1] * (n)
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5


for i in range(1, n):

    dp[i] = min(next2, next3, next5)
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n-1])

