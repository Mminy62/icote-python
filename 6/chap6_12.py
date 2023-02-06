'''
문제 - A의 가장 작은 값과 B의 가장 큰 값을 최대 K번 바꿔치기 했을 때, 남은 원소
N이 10만 이므로 sorted를 써서 가장 작거나 큰걸 바꾸자.
A의 합이 가장 큰 걸로

input
5 3
1 2 5 4 3
5 5 6 6 5
'''

n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))

