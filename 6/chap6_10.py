'''
chap6 실전문제 "위에서 아래로"
input
3
15
27
12
'''
n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))
result.sort(reverse=True)

print(*result)