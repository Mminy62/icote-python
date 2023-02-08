'''
거리의 평균값을 구해 근접한 집의 위치를 반환시키려 했다.
하지만, N이 20만이므로, 극단적인 거리 차이가 있을 시엔, 평균값보다 중앙값이 좋다.
-> 중앙값(median)은 중심경향치(center tendency)의 하나로 전체 데이터 중 가운데에 있는 수치 값이다.
직원이 100명인 회사에서 직원들 연봉 평균은 5천만원인데 사장의 연봉이 100억인 경우, 회사 전체의 연봉 평균은 1억 4851만 원이다.
이처럼 극단적인 값이 있다면 중앙값이 평균값보다 유용하다.[위키백과-중앙값]

input
4
5 1 7 9
'''

n = int(input())

house = list(map(int, input().split()))
house.sort()

if n % 2 == 0:
    avg = (house[(n//2)-1] + house[n//2]) / 2
    be = abs(avg - house[n//2-1])
    af = abs(avg - house[n//2])
    if be <= af:
        med = house[n//2-1]
    else:
        med = house[n//2]
else:
    med = house[n//2]

print(med)





