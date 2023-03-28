'''
고정점 찾기
풀음

9
-4 -1 2 3 7 9 10 11 13
-> 2
index < value:
    end = index - 1

10
-4 -3 -2 -1 0 2 3 4 5 9
index > value
start = index + 1
-> 9

5
-15 -4 2 8 13

'''

n = int(input())
nums = list(map(int, input().split()))

start = 0
end = n - 1

while start <= end:
    mid = (start + end) // 2
    value = nums[mid]
    if mid < value:
        end = mid - 1
    elif mid > value:  # index > value:
        start = mid + 1
    else:
        print(value)
        break


