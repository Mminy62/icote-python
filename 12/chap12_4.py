'''
 열쇠를 회전, 이동하여 자물쇠의 홈에 맞게 채우는 것.
    자물쇠의 영역을 벗어난 열쇠는 영향을 주지 않지만 정확히 돌기와 홈이 일치해야하며,
    열쇠의 돌기와 자물쇠의 돌기가 만나선 안된다.
    또한 자물쇠의 모든 홈을 채워 비워있는 곳이 없어야한다.
    즉, 열쇠가 자물쇠의 영역은 벗어나도 되지만, 자물쇠 전체의 홈은 제대로 채워야한다.
    열쇠로 열 수 있으면 true 없으면 false
'''
import itertools

def rotate_matrix(keys):
    n = len(keys)
    m = len(keys[0])
    matrix = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            matrix[j][n-1-i] = keys[i][j]

    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def check(matrix):
    #원래의 자물쇠 길이
    lock_length = len(matrix)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if matrix[i][j] != 1:
                return False
    return True



def solution(key, lock):
    answer = False

    #열쇠 돌기의 수가 자물쇠의 구멍보다 작은 경우 (아예 못채우는 경우)
    if list(itertools.chain(*key)).count(1) < list(itertools.chain(*lock)).count(0):
        return False

    n = len(lock)
    m = len(key)

    temp_matrix = [[0] * n * 3 for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            temp_matrix[i+m][j+m] = lock[i][j]

    for _ in range(4):
        key = rotate_matrix(key)

        for x in range(n * 3 - m):
            for y in range(n * 3 - m):
                for i in range(m):
                    for j in range(m):
                        temp_matrix[x+i][y+j] += key[i][j]

                if check(temp_matrix):
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            temp_matrix[x + i][y + j] -= key[i][j]

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))