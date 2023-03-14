'''
input

'''
from collections import deque

def get_next_pos(pos1, pos2, board):# 현재 위치에서 다음 위치로 이동 가능한 것
    n = len(board) - 2
    x1, y1 = pos1
    x2, y2 = pos2
    next_pos = []

    # 일단 상하좌우 확인
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx1, nx2 = x1 + dx[i], x2 + dx[i]
        ny1, ny2 = y1 + dy[i], y2 + dy[i]
        if nx1 <= 0 or nx1 > n or nx2 <= 0 or nx2 > n or ny1 <= 0 or ny1 > n or ny2 <= 0 or ny2 > n:
            continue
        if board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
            continue
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})

    # 회전 경우
        # 블록 상태가 가로인 경우
    if x1 == x2:
        # 위로 회전 가능한 경우
        ux, uy = [-1, 0]
        ux1, uy1 = x1 + ux, y1 + uy
        ux2, uy2 = x2 + ux, y2 + uy
        if board[ux1][uy1] == 0 and board[ux2][uy2] == 0: # 회전 가능
            pos1 = {(x1 - 1, y1 + 1), (x2, y2)}
            pos2 = {(x2 - 1, y2 - 1), (x1, y1)}
            next_pos.append(pos1)
            next_pos.append(pos2)

        # 아래로 회전 가능한 경우
        dx, dy = [1, 0]
        dx1, dy1 = x1 + dx, y1 + dy
        dx2, dy2 = x2 + dx, y2 + dy
        if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:  # 회전 가능
            pos1 = {(x2, y2), (x1 + 1, y1 + 1)}
            pos2 = {(x1, y1), (x2 + 1, y2 - 1)}
            next_pos.append(pos1)
            next_pos.append(pos2)

    else: # 블록이 세로인 경우
        # 오른쪽 회전 가능한 경우
        rx, ry = [0, 1]
        rx1, ry1 = x1 + rx, y1 + ry
        rx2, ry2 = x2 + rx, y2 + ry
        if board[rx1][ry1] == 0 and board[rx2][ry2] == 0:  # 회전 가능
            pos1 = {(x2, y2), (x1 + 1, y1 + 1)}
            pos2 = {(x1, y1), (x2 - 1, y2 + 1)}
            next_pos.append(pos1)
            next_pos.append(pos2)
        # 왼쪽 회전 가능한 경우
        lx, ly = [0, -1]
        lx1, ly1 = x1 + lx, y1 + ly
        lx2, ly2 = x2 + lx, y2 + ly
        if board[lx1][ly1] == 0 and board[lx2][ly2] == 0:  # 회전 가능
            pos1 = {(x1 + 1, y1 - 1), (x2, y2)}
            pos2 = {(x2 - 1, y2 - 1), (x1, y1)}
            next_pos.append(pos1)
            next_pos.append(pos2)

    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    visited = []

    # new_board 세팅
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    for i in range(n + 2):
        print(new_board[i])
    start = {(1, 1), (1, 2)}
    cost = 0
    q = deque()
    q.append((start, cost))
    visited.append(start)

    while q:
        pos, cost = q.popleft()
        pos1, pos2 = pos
        if (n, n) in pos:
            return cost
        # 현재 위치에서 bfs 시작
        next_list = get_next_pos(pos1, pos2, new_board)
        for next_pos in next_list:
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return cost

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))