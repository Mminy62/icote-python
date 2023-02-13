'''
x의 수가 크기 때문에 해당 원소를 이진 탐색으로 찾는다.
bisect 라이브러리를 활용하면 이진 탐색을 직접 구현할 필요 없이 가능하다.

input
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''
## 이진탐색으로 구현

import sys

def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n-1)

    if a == None:
        return 0
    else:
        b = last(array, x, 0, n-1)
        return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if mid == 0 or target > array[mid - 1] and array[mid] == target:
        # and 때문에 mid가 target 값이고 왼쪽값이 target 보다 작은 경우 이므로 가장 작은 인덱스를 보내게된다.
        return mid

    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2

    if mid == n-1 or target < array[mid-1] and target == array[mid]:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)

n, x = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))
count = count_by_value(nums, x)

if count == 0:
    print(-1)
else:
    print(count)

## bisect 이용
# from bisect import bisect_left, bisect_right
# import sys
# n, x = map(int, input().split())
# nums = list(map(int, sys.stdin.readline().split()))
#
# lindex = bisect_left(nums, x)
# if lindex == n:
#     print(-1)
# else:
#     rindex = bisect_right(nums, x)
#     print(rindex-lindex)
