'''
(풀이참조)
거리 자체를 mid로 설정
처음이랑 끝 나누기 //2 한 인덱스에 있는 값에 설치,,?

mid = end - start


input
5 3
1
2
8
4
9

dp 와 이진탐색을 섞은 것 처럼
맨 앞 장소에서부터 하나씩 더해가면서 오른쪽 범위로만 계속 탐색

start ~ mid 까지의 거리가

2개면 설치 처음, 끝 일단 해놓고

start = 1
end = house[-1] - house[0]

mid = start + end // 2 -> 거리 자체를 중간으로 줄여서
일단 시작은 s = array[0]
s + mid 하는 간격

if array[i] >= s + mid:
    count += 1
if count >= c:
    result = mid
    break

n <= 20만
집 거리 <= 10억
'''
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2 # 거리 자체로
    s_point = house[0]
    count = 1

    for i in range(1, n):
        if house[i] >= s_point + mid:
            count += 1
            s_point = house[i]
    if count >= c:
        result = mid # 충분하다는 뜻이니까 거리 줄여도 됨
        start = mid + 1

    else: # 불충분 -> end = 3
        end = mid - 1


print(result)