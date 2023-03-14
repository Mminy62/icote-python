'''
permutations 사용

연산자의 갯수에 따라 1,2,3,4 로 나열한 뒤에
#0 + 1 - 2 * 3 /

input

'''

from itertools import permutations

n = int(input())
nums = list(input().split())
result = []

operators = list(map(int, input().split()))

ops_menu = ['+', '-', '*', '//']
ops_list = []

for i, op in enumerate(operators):
    for j in range(op):
        ops_list.append(ops_menu[i])

ops_list = list(permutations(ops_list, len(ops_list)))

for ops in ops_list:
    temp = nums[0]
    for i in range(len(ops)):
        if ops[i] == '//' and temp[0] == '-':
            temp = temp[1:]
            temp = str(eval(temp + ops[i] + nums[i+1]))
            temp = '-' + temp
        else:
            temp = str(eval(temp + ops[i] + nums[i + 1]))

    result.append(temp)

result = list(map(int, set(result)))
print(max(result))
print(min(result))
