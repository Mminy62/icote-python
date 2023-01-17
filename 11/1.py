#정답 최적 코드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력


#내 코드
#모두가 1 일 때, 최악 O(n)
#모두가 n 만큼 일 때, 최저 O(1) 5 (5 5 5 5 5)

n = int(input())
data = list(map(int, input().split()))
data.sort() # 공포도를 낮은 것부터 확인, 오름차순

answer = 0 # 총 그룹 수

while data: 
    if data[0] > len(data): #공포감 정도에 비해 사람 수가 적으면 마을에 냅둔다.
        break
    else:
        group = data[:data[0]] #현재의 모험가 그룹
        data = data[data[0]:] #모험가 대상
        if max(group) <= len(group):
            answer += 1

print(answer)
