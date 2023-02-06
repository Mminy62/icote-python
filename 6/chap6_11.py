'''
문제 - 성적이 낮은 순으로 이름 출력
input
2
홍길동 95
이순신 77
'''

n = int(input())
result = []
for _ in range(n):
    name, score = input().split()
    result.append([name, int(score)])

result = sorted(result, key=lambda x: x[1])

for data in result:
    print(data[0], end=' ')