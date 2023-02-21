'''
풀이 참조

합성수 = 소인수들만의 곱으로 이루어진 수
소인수가 2,3,5 이므로 각 못생긴 수에 2, 3, 5를 곱한 수도 못생긴 수 이다.

못생긴 수의 후보들 중 2, 3, 5를 곱하여 가장 작은 수가 다음 자리에 가게 된다.
또한 하나의 못생긴 수에 대해 2, 3, 5를 다 곱해볼 수 있도록 해야한다.
그러므로 n번까지 이 과정을 반복하면 n번째 자리를 찾을 수 있다.
'''

n = int(input())
ugly = [1] * n # 못생긴 수를 담는 테이블 (dp 테이블)
next2, next3, next5 = 2, 3, 5
i2 = i3 = i5 = 0

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)

    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3: # 들어갔으니 바꿔줘야함
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])

