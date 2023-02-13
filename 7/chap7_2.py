'''
절단기에 설정하는 높이가 클수록 좋은 것이므로,
제일 큰 것부터 작은것까지의 차이로 높이를 설정한다
(작은 길이가 짤린다는 건 그만큼 H가 작아진다는 소리이므로)
19 18 17 16 15
제일 갯수를 적게 자르는게 결국 높이도 지키는거 아닐까?
10 10 10 10
4 면 9센치
500 2

input
4 6
19 15 10 17
'''
import heapq
import sys

n, m = map(int, input().split())
temp = list(map(int, sys.stdin.readline().split()))
reversed(temp)
heapq.heapify(temp)

print(temp)

# for data in temp:
#     heapq.heappush(max_heap, data)
#
# while m > 0:
#     popvalue = heapq.heappop(max_heap)
#     if popvalue > 0:
#         heapq.heappush(max_heap, popvalue-1)
#         m -= 1
# print(max_heap)