'''
sort 후에 가장 큰 수를 k번 하고 다음 큰 수를 하면 됨.
k <= m
m번 더하고 같은 수는 k번까지만 더할 수 있음. 연속해서

input
5 8 3
2 4 5 4 6
'''
n, m, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort(reverse=True)
result = 0

# 몫, 하나 더하는걸 세트로 봐야해

if m == k:
    result += k * nums[0]

else:
    count = (m // (k+1)) * k
    result += count * nums[0]
    count += m % (k + 1)
    result += (m // k) * nums[0] * k + (m - (m//k)*k) * nums[1]

print(result)
print(int(6/4))
