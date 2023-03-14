from collections import deque
'''
설치/삭제할때마다 기둥과 보의 조건 체크
바닥에 보를 설치하는 경우는 없다

처음엔 기둥과, 보를 따로 큐에 넣어놓고 기둥/보의 설치/삭제 때마다 따로 확인 해줬는데 이 작업이 직관적이나 너무 코드가 중복적이다.
또한 설치/삭제 함수를 다 따로 만들었다. 
그러므로 시간과 메모리를 줄이기 위해 답지대로 
체크 함수를 만들고, 일단 기둥과 보 전체를 다 넣어서 갖고 다녀야하기에 한번에 answer에 넣어서 하는게 더 타임에러를 줄인다.

// 기둥과 보 둘다 합치면 1000정도일 수도 있기 때문에
input [x, y, a, b]
a -> 기둥 0/보 1 구분
b -> 삭제 0/설치 1
'''
## 함수를 부르는 게 시간이 많이 걸릴 것 같아서 주석처리 해봤다.
def check(answer):
    # 기둥과 보의 좌표를 보고 해당 기준에 성립하는지 -> 아닌게 나오면 좌표, 맞으면 0
    # 기둥이라면
    for x, y, stuff in answer:
        if stuff == 0:
            # 바닥 위에 / 보의 한쪽 끝에 / 또 다른 기둥 위에
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else: # 아닌 경우
                return False

        # 보 라면
        if stuff == 1:
            # 양쪽 끝이 다른 보와 동시에 연결 / 한쪽 끝이 기둥 위
            if ([x-1, y, 1] in answer and [x+1, y, 1] in answer) or [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            else:
                return False

    return True

def solution(n, build_frame):
    answer = []
    # gidung = deque([]) # 좌표를 기준으로 위로 하나
    # bo = deque([]) # 좌표를 기준으로 오른쪽으로 하나

    # 설치할거면 해당 좌표만 확인
    # 삭제할거면 전체 gidung, bo 확인
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 1:# 설치
            # 일단 설치 해보고 아니면 제거
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])

        if b == 0:# 삭제
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    return sorted(answer)


build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(5, build_frame))
