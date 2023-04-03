'''
두 개의 문자열 A와 B가 주어졌을 때, 문자열 A를 편집하여 문자열 B로 만들고자 합니다.
문자열 A를 편집할 때는 다음의 세 연산 중에서 한 번에 하나씩 선택하여 이용할 수 있습니다.
삽입(Insert): 특정한 위치에 하나의 문자를 삽입합니다.
삭제(Remove): 특정한 위치에 있는 하나의 문자를 삭제합니다.
교체(Replace): 특정한 위치에 있는 하나의 문자를 다른 문자로 교체합니다.
이때 편집 거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미합니다.
문자열 A를 문자열 B로 만드는 최소 편집 거리를 계산하는 프로그램을 작성하세요.
예를 들어 "sunday"와 "saturday"의 최소 편집 거리는 3입니다.

A -> B
이걸 dp로 어떻게?>..
편집거리,,
sunday saturday
a -> b를 비교할 때, 다른 부분의 인덱스
일단 길이 비교를 통해 적으면 무조건 삽입이 일어난다.
6, 8
a, t삽입
satu n -> r(교체)
saturdat 해서 3

길이가 작아도 삭제가 일어나는 건 반드시 필요
sunday
saturday

s
u, a 우째 교체
그냥 공통된걸 빼보자 -> s, u, day
s, u, d, a, y

s (a) (t) u (r) d a y
공통 찾기
a -> b니까
b에 문자중 a에서 있으면 삭제, a가 없을 때까지 혹은 b가 없을 때까지 한다.
tac
cat
1


'''

a = input()
b = input()

n = len(a) + 1
m = len(b) + 1
dp = [[0] * m for _ in range(n)]

# 초기화
for i in range(n):
    dp[i][0] = i
for j in range(m):
    dp[0][j] = j

for i in range(1, n):
    for j in range(1, m):
        if a[i-1] != b[j-1]:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = dp[i-1][j-1]

print(dp[n-1][m-1])


