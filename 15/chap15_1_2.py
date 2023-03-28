'''
n, x가 주어지고
n개의 문자에서 x가 등장하는 횟수를 구해야한다.
중간 값을
input
7 2
1 1 2 2 2 2 3
'''

'''
x를 찾아도 기준을 앞으로 해야되나..?
찾는 문자보다 하나 작은 값, 하나 큰 값
찾는 문자의 하나 작은 값.. 하나 큰 값

기준은 x보다 작으면 end,
mid 로 확인한 값이 x보다 작고, mid + 1이 x이면 됨

mid로 구해서 count 
mid + 1이 큰 값이면 
111 22222 44 55 

mid 로 확인한 값이 
mid + 1 or mid - 1이 해당 값이면 맞음
해당 값이면 cnt ..? 
두개로 나눠서 할까 

(풀음)

'''

n, x = map(int, input().split())
nums = list(map(int, input().split()))

ls = 0
le = n - 1
lcount = 0
# lbinary
while ls <= le:
    mid = (ls + le) // 2
    if nums[mid] == x:
        lcount += 1
        le = mid - 1
    elif nums[mid] < x:
        ls = mid + 1
    else:
        le = mid - 1


# rbinary
rs = 0
re = n - 1
rcount = 0
# lbinary
while rs <= re:
    mid = (rs + re) // 2
    if nums[mid] == x:
        rcount += 1
        print(mid, rcount)
        rs = mid + 1
    elif nums[mid] < x:
        rs = mid + 1
    else:
        re = mid - 1

print(lcount + rcount)