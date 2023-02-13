'''
부품 즉, 탐색할 데이터의 범위가 100만
-> 데이터가 1000만개는 안넘어가는데 꼭 이진탐색으로 해야할까? -> O(N)이하로 해결하지 않으면 안됨
=> O(n+k)로 계수 정렬로도 해결할 수 있다.


input
5
8 3 7 9 2
3
5 7 9

'''

import sys
n = int(sys.stdin.readline())
item_list =list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
check_list =list(map(int, sys.stdin.readline().split()))

def binary_search(item_list, check_list):

    result = []

    for data in check_list: # O(M * logN)
        start = 0
        end = len(item_list) - 1
        mid = (start + end) // 2

        while start <= end:
            if item_list[mid] == data:
                result.append("yes")
                break
            if data > item_list[mid]:
                start = mid + 1
            if data < item_list[mid]:
                end = mid - 1

            mid = (start + end) // 2

        if start > end:
            result.append("no")

    return result


answer = binary_search(sorted(item_list), check_list)
print(*answer)