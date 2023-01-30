
def check(matrix):
    #통과하면 연산 가능




    return True

def solution(n, build_frame):
    #return이 배열이므로 굳이 matrix를 만들 필요가 없어
    answer = []



    for data in build_frame:
        #a: 기둥 0 보 1, b: 삭제 0 설치 1
        x, y, a, b = data

        nx = x + dx[a]
        ny = y + dy[a]

        if a == 0 and b == 1:
            #기둥인 경우 1) 시작 좌표가 바닥 2)시작 좌표가 기둥인 경우 3) 시작 좌표가 보인 경우
            #시작점만
            print(x, y, a, b)
            print(nx, ny)
            if x == 0 or matrix[x][y] == 0:
                matrix[x][y] = 0
                matrix[nx][ny] = 0

            elif matrix[x][y] >= 1:
                matrix[nx][ny] = 0

        elif a == 0 and b == 0: #삭제인 경우
            #양쪽을 다 삭제해?...미친






    return matrix

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
matrix = solution(5, build_frame)

# Print matrix
for i in range(len(matrix)):
    print(matrix[i])