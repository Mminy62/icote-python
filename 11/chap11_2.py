'''
숫자 사이에 +, * 를 넣어 가장 큰 수를 만드는 것

'''
n = list(map(int, input()))
result = n[0]
for data in n[1:]:
    if data <= 1 or result <= 1:
        result += data
    else:
        result *= data

print(result)
