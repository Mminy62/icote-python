'''
  # 벽의 취약 지점을 기준으로

    한 지점마다 시작지점을 바꿔
    시작지점마다 사람들을 돌려서
    순열리스트에서
    한명씩 빼서 4명 다해보고 그래도 안되면 시작지점 변경

    한명으로 안되면 두명 추가할땐,
    cnt 를
'''

from itertools import permutations

def solution(n, weak, dist):
    answer = []
    weak_point = weak[:]

    for v in weak:
        weak_point.append(n + v)
    wL = len(weak)

    for i, v in enumerate(weak):
        # 시작 지점 + f 의 dist 더하기
        for friend in permutations(dist):
            start = v
            finish = weak_point[i + wL - 1]
            cnt = 0
            temp = 0
            for distance in friend:
                cnt += 1
                temp = start + distance
                if temp < finish:
                    # weakpoint중 다음 걸로
                    next = list(filter(lambda w: w > temp, weak_point))
                    if next:
                        start = next[0]
                        continue
                    else: # next weak point 가 없는 경우
                        break
                else: # 넘은 경우
                    answer.append(cnt)
                    break

    if not answer:
        return -1
    return min(answer)

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
