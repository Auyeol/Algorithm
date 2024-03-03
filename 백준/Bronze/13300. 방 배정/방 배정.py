# 방 배정

# 1학년 ~ 6학년이 묵을 방 배정
# 남-남, 여-여, 한 방에는 같은 학년들을 배저ㅜㅇ
# 한 방에 한 명만 배정도 가능
# 한 방에 배정할 수 있는 최대 인원 수 K, 조건에 맞게 모든 학생을 배정하기 위한
# 최소 개수를 구하는 프로그램 작성

# K = 2 일 때 12개의 방 필요
import sys
N, K = map(int, sys.stdin.readline().split())
G = [[] for _ in range(7)]  # 1학년 ~ 6학년 학생 수, 0번은 사용 X
for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    G[Y].append(S)
total = 0
for i in range(1, len(G)):
    if G[i]:
        m_cnt = G[i].count(1)
        w_cnt = G[i].count(0)
        # print(f'{G[i]}, K = {K}')
        # print(m_cnt, w_cnt)

        while m_cnt > 0:
            # print('m_cnt',m_cnt)
            m_cnt -= K
            total += 1
            # print('m total',total)
        while w_cnt > 0:
            # print('w_cnt',w_cnt)
            w_cnt -= K
            total += 1
            # print('w total ',total)


print(total)
