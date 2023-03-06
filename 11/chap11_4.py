n = int(input())

units = list(map(int, input().split()))

units.sort()

target = 1
for unit in units:
    if target < unit:
        print(target)
        break
    target += unit
