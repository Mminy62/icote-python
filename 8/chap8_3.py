''' 풀이 참조'''
n = int(input())
d = [0] * (n+1)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = d[n-2] * 2 + d[n-1]

print(d[n])

