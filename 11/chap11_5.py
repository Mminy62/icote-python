'''
P로 하고
같은 것들끼리는 빼면 좋은데,,,
8 5
1 5 4 3 2 4 5 2
'''
from itertools import combinations
n, m = map(int, input().split())

balls = list(map(int, input().split()))
cnt = len(list(combinations(balls, 2)))

for a, b in list(combinations(balls, 2)):
    if a == b:
        cnt -= 1

print(cnt)


