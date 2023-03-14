'''
체스판과 같은 왕실 정원
나이트는 말을 타고 있기에 이동할 땐 L자 형태로만 이동 가능
정원 밖으로 나갈 수 없다.
특정한 위치에서 다음과 같은 2가지 경우로 이동 가능
1. 수평으로 두칸 이동후 수직으로 한칸 이동  --ㅣ
2. 수직으로 두칸 이동 후 수평으로 한칸 이동

나이트의 위치가 주어지면, 거기서 이동 가능한 위치의 수 출력

'''
n = 8
graph = [[1] * n for _ in range(n)]

pos = input()

x = int(pos[1]) - 1
y = ord(pos[0]) - 97

dx = [-2, 1, 2, -1, -2, -1, 2, 1]
dy = [1, 2, -1, -2, -1, 2, 1, -2]
cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
    else:
        cnt += 1

print(cnt)