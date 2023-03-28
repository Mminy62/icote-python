'''
적어도 짤린 떡의 길이가 m이상
떡의 높이 총 합은 항상 m이상

height를 binary search로 알아와서 해보고
적으면 다시 늘리고
start = mid + 1
너무 많으면 줄이고
end = mid - 1

input
4 6
19 15 10 17
'''

# def binary_search(height):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if rices[mid] == height:
#
#     return height
# n <= 100만 m <= 20억
# n <= 100만

n, m = map(int, input().split())
rices = list(map(int, input().split()))
rices.sort()
start = 0
end = len(rices) - 1

while start <= end:
    mid = (start + end) // 2

    height = rices[mid]

    temp = list(filter(lambda x: x >= height, rices))
    result = sum(temp) - (height * len(temp))

    if result == m:
        print(height)
        break
    elif result < m:
        end = mid - 1
    else:
        start = mid + 1
