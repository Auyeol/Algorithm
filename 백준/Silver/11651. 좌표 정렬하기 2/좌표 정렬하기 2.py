# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로,
# y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력
import sys
N = int(sys.stdin.readline())   # N을 입력받음
arr = []                        # 결과값을 집어넣을 빈 리스트 생성
for _ in range(N):              # N만큼 반복
    x, y = map(int, sys.stdin.readline().split())   # x좌표, y좌표를 입력받는다.
    arr.append((y, [x,y]))      # 튜플형태로 ( y좌표, [x,y]의 좌표값) 들어가게 저장

arr.sort()                      # .sort() 사용하여 정렬

for elem in arr:
    print(*elem[1])             