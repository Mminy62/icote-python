'''
input
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

https://dev-note-97.tistory.com/125
sort 함수 key 여러개 지정 가능 -> 우선, 차선책

print(sorted(array, key=lambda x: (x[0], x[1]))) # 0번, 1번 키(알파벳, 숫자)
print(sorted(array, key=lambda x: (x[0], x[2]))) # 0번, 2번 키(알파벳, 한글)

# 출력
# [('a', 3, '다'), ('a', 7, '가'), ('b', 1, '나'), ('c', 2, '라'), ('c', 3, '가')]
# [('a', 7, '가'), ('a', 3, '다'), ('b', 1, '나'), ('c', 3, '가'), ('c', 2, '라')]
'''

n = int(input())
score_list = []
for _ in range(n):
    temp = input().split()
    temp[1:] = map(int, temp[1:])
    score_list.append(temp)


score_list.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for data in score_list:
    print(data[0])

