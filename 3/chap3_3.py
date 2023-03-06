n, k = map(int, input().split())

remain = n % k
n -= remain

count = remain
while n > 0:
    if n == 1:
        break
    n = n // k
    count += 1


print(count)