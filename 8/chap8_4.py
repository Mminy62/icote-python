'''
input
2 15
2
3

3 4
3
5
7
'''
n, m = map(int, input().split())

d = [10001] * 10001
coins = []
d[0] = 0
for _ in range(n):
    v = int(input())
    coins.append(v)

for i in range(min(coins), m + 1):
    for c in coins:
        if d[i - c] != 10001:
            d[i] = min(d[i], d[i - c] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])