'''
풀이 참조

* 탑다운 방식
바텀없으로 1일차부터 생각하게 되면 경우의 수가 너무 많아진다.
뒤쪽부터 매 상담에 대해 현재 날짜부터 뒤까지의 경우를 파악하면 앞에선 바로 다음 항만 고려해주면 된다.

- 당일 포함 유뮤 -> (현재 날짜 + 상담 일수 - 1) <= N 이면 현재 날짜 pay 더하기
    - 당일 더한 것에서 상담일수 만큼의 간격을 가진 다음 항 포함 유무
    -> dp[현재 날짜 + 상담 일수 -1] 더하기

'''

n = int(input())

dp = [0] * (n+1)
array = [[0]]
max_value = 0

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n, 0, -1):
    time = i + array[i][0]
    if time <= n + 1:#현재 날짜가 포함되는 경우
        dp[i] += array[i][1]
        if time <= n:# 현재 날짜의 상담 간격만큼 더해주는 경우
            dp[i] += dp[time]
        dp[i] = max(dp[i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)