'''
# for unit 단위만큼
길이~ 1 까지 1만큼씩
8개의 길이
for i in range(0, len(s), unit)
i: i + unit -> 0:2
pre =
pre = s[i:unit]

pre != pos -> pre = pos, cnt = 1
pre != pos and cnt != 1: result += (cnt + pre)
                cnt == 1: result += pre
마지막 글자인 경우 pre
마지막 글자 # 현재가 pos pre == pos 인 상태, cnt !=1 이면 그거고 아니면 pos로

'''
s = input()

unit_list = len(s) // 2

result = ''
pre = ''
answer = []

for unit in range(1, unit_list + 1):# 1-8까지
    cnt = 1
    pre = s[:unit] # s[0:8] 0-7 0-15
    # for i in range(8, 16, 8):
    #   pos = s[8: 16] 8-15

    result = ''
    for i in range(unit, len(s), unit):
        pos = s[i:i + unit]

        if pre == pos: #압축
            cnt += 1

        if pre != pos: #단위 내용 변경
            if cnt != 1:
                result += (str(cnt) + pre)
            else:#cnt == 1
                result += pre
            cnt = 1
            pre = pos
    # 마지막 단위 확인
    if cnt != 1:
        result += (str(cnt) + pre)
    else:
        result += pre


    print(unit, result)
    answer.append(len(result))

print(min(answer))

