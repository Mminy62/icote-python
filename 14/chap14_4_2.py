import heapq

n = int(input())
nums = []

for _ in range(n):
    heapq.heappush(nums, int(input()))

result = 0
for _ in range(n-1):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    temp = a + b
    result += temp
    heapq.heappush(nums, temp)

print(result)