'''
공포도가 x인 모험가는 반드시 x명이상으로 구성
최대 몇개의 그룹을 만들 수 있는가.
각 모험가의 공포도가 다음과 같다고 가정하자.

공포도가 가장 높은 것을 기준으로 앞에서부터 묶으면 되지 않나.?
단 모든 모험가가 다 담기진 않아도 된다.
그럼 오름차순으로 정리
1 2 2 2 3

1 2 2

'''

n = int(input())
mems = list(map(int, input().split()))

mems.sort()
cnt = 0
group = 0
for mem in mems:
    group += 1
    if group >= mem:
        cnt += 1
        group = 0

print(cnt)