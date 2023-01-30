n = input()

#list를 안씌운 map만 한 코드가 더 시간이 많이나온다 왜지?
'''
front = map(int, n[0:len(n)//2])
back = map(int, n[len(n)//2:])
'''
front = list(map(int, n[0:len(n)//2]))
back = list(map(int, n[len(n)//2:]))

if sum(front) == sum(back):
    print('LUCKY')
else:
    print('READY')