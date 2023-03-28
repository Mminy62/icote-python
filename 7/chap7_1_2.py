n = int(input())
items = list(map(int, input().split()))

m = int(input())
searchs = list(map(int, input().split()))

items.sort()

def binary_search(start, end, search):
    while start <= end:
        mid = (start + end) // 2
        if items[mid] == search:
            return "yes"

        if search < items[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return "no"

answer = []
for search in searchs:
    answer.append(binary_search(0, len(items)-1, search))

print(*answer)



