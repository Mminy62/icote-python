'''
공유기 설치의 인접한 거리를 mid값으로 설정하자는 것.
거리의 최대값은 max - min
거리의 최소값은 min 1
(풀이 참조)
input
5 3
1
2
8
4
9

5 2
1
2
8
4
9

5 3
999999980
999999985
999999991
999999996
1000000000
'''

from bisect import bisect_left
import sys
array = []
n, c = map(int, sys.stdin.readline().split())
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()

def binary_search(array, n, c):
    start = 1
    end = array[-1] - array[0]
    result = 0

    while start <= end:
        mid = (start + end)//2
        value = array[0]
        count = 1

        for i in range(1, n):
            if array[i] >= value + mid:
                value = array[i]
                count += 1
            # if count == c: #n까지 탐색하는게 시간이 걸릴 것 같아서 break문을 넣어줬는데 시간엔 별 차이 없음..
            #     break
        if count >= c:
            start = mid + 1
            result = mid
        else:# count < c #gap 좀 낮추기
            end = mid - 1

    return result

print(binary_search(array, n, c))

