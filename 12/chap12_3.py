def solution(s):
    '''
    같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현
    "aabbaccc"의 경우 "2a2ba3c" 1은 생략
    반복되는 문자가 적은 경우 압축률이 낮다. 

    - 1개일때, 2개일때, 등의 단위를 돌아가면서
    해보는 것.
    '''
    length = len(s)
    answer = len(s)

    #문자열 끊는 단위
    for i in range(1, length // 2 + 1): #범위 생각
        count = 1
        result = ''
        before = s[0:i]

        for j in range(i, length, i): #i 만큼 끊어서 표현
            if before == s[j:j + i]:
                count += 1
            else:
                if count == 1:
                    result += before
                else:
                    result += str(count) + before

                count = 1
                before = s[j:j + i]

        result += str(count) + before if count >= 2 else before

        print(result)
        answer = min(answer, len(result))
        print(answer)
    return answer

solution("xababcdcdababcdcd")

