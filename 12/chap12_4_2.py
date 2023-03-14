'''
lock의 9배 만한 Matrix를 만들어서 key의 방향을 4번 바꾸고 9배 크기의 Matrix를 이동시킨다.

- matrix 초기화
- Key 방향 돌리기
    - key 이동 시키기

'''
def rotate_key(key, m):
    graph = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            graph[j][m-i-1] = key[i][j]

    return graph

def check(matrix, n):

    # matrix 가운데 자물쇠 부분
    for i in range(n, n + n):
        for j in range(n, n + n):
            if matrix[i][j] != 1:
                return False
    return True

def solutions(key, lock):
    # key - m, lock - n
    # m <= n 항상 ## lock의 크기가 더 크다 ## 시간복잡도 n으로 계산한 거니까 괜춘
    # 0 이 홈 1이 돌기 ## 가운데 부분이 전부 1이면 통과
    m = len(key)
    n = len(lock)

    #lock 의 9배 크기의 matrix 생성
    matrix = [[0] * n * 3 for _ in range(n * 3)]

    # matrix 가운데에 Lock으로 초기화
    for i in range(n, n + n):
        for j in range(n, n + n):
            matrix[i][j] = lock[i-n][j-n]

    for i in range(4):
        key = rotate_key(key, m)

        # key의 matrix 이동
        for r in range(0, n * 2 + 1):
            for c in range(0, n * 2 + 1):

                for i in range(m):
                    for j in range(m):
                        matrix[i + r][j + c] += key[i][j]

                if not check(matrix, n):  # 틀리면
                    for i in range(m):
                        for j in range(m):
                            matrix[i + r][j + c] -= key[i][j]
                else:
                    return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solutions(key, lock))