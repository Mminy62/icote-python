'''
스테이지에 도달했으나, 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수

- 현재 머물고 있는 스테이지 정보 -> input
- 스테이지 갯수 n <= 500
- 사람 인원 <= 20만
- 스테이지 정보는 1~ N+1까지 들어있다 -> n + 1 은 마지막까지 클리어한 사용자

- 실패율이 같으면 작은 번호의 스테이지가 먼저 오도록 한다.
- 스테이지에 도달한 유저가 없으면 해당 스테이지의 실패율은 0

1번 스테이지 -> 8명중 1명
1/8
2번 -> n명 줄여서
3/7

실패율이 높은 순으로 번호를 정렬한다.
스테이지 번호와 함께 실패율 저장

key=lambda x : (-x[1],x[0])

20만 한번 for문으로 돌려서

20만 * 500
'''
def solution(N, stages):

    answer = []
    result = []
    # 스테이지의 갯수 N
    #
    pops = len(stages)
    for i in range(1, N + 1):
        not_clear = len(list(filter(lambda x: i == x, stages)))
        fail = not_clear/pops
        pops -= not_clear
        result.append((i, fail))

    for x in sorted(result, key=lambda x: (-x[1], x[0])):
        answer.append(x[0])

    return answer


print(solution(4, [4,4,4,4,4]))