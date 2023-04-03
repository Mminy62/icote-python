'''

dp 테이블에 각 숫자에 대한 연산 횟수를 집어넣고
진행한다.

bottom-up 방식

'''

n = int(input())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    num = i
    cnt = 0
    temp = []
    if num % 5 == 0:
        temp.append(dp[num // 5])
    if num % 3 == 0:
        temp.append(dp[num // 3])
    if num % 2 == 0:
        temp.append(dp[num // 2])

    temp.append(dp[num-1])

    dp[i] = 1 + min(temp)

print(dp[n])

