'''
(풀이참조)
keywords에 물음표가 있는 거니까

인덱스를 길이별로 만들어서 최대 길이 + 1만큼 만들고
각 array sort 시키기
'''
from bisect import bisect_right, bisect_left

def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()


    for keyword in queries:
        length = len(keyword)
        #keyword 별로 해당되는거 저장 나중에 count 하고 일단 temp
        cnt, left, right = 0, 0, 0

        if keyword[-1] == "?":
            # fr??? 접미사
            ## 효율성 테스트 시간 초과
            ## left만 알아서 array에서 길이가 같은 배열에 처음부터 끝까지 같은걸 찾는 것이 비효율적
            ## keyword 자체를 배열에 넣고 그 시작점부터 right까지로 하면 될 것 같음..
            # left = bisect_left(keyword.replace("?", "{"), "{")
            #
            # for word in array[length]:
            #     if word[:left] == keyword[:left]:
            #         cnt += 1

            left = bisect_left(array[length], keyword.replace("?", "a"))
            right = bisect_right(array[length], keyword.replace("?", "z"))

        else: # 접두사
            keyword = keyword[::-1]
            left = bisect_left(reversed_array[length], keyword.replace("?", "a"))
            right = bisect_right(reversed_array[length], keyword.replace("?", "z"))

        cnt = right - left
        print(keyword, right, left)
        answer.append(cnt)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
