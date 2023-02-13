'''
고정점이없으면 -1
있으면 내놓기
고정점 구하기 인덱스와 같은 거니까 일단 양수
백만이니까 1초로 되지 않나?.. 순차로 돌려서 나오면 return

이진탐색으로 범위를 반으로 나눈 다음에
음수의 인덱스를 알아내서 있으면 그 뒤부터 검사
없으면 앞부터 검사

인덱스 값이 0인경우 0이어야 고정점. 아니면 none
input
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
'''
import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))

def binary_search(array, n, start, end):
    mid = (start + end)//2

    if start > end:
        return -1

    if array[mid] <= 0 or array[mid] < mid:
        return binary_search(array, n, mid + 1, end)

    elif array[mid] == mid:
        return mid

    elif array[mid] > mid:
        return binary_search(array, n, start, mid - 1)


print(binary_search(array, n, 0, n-1))
