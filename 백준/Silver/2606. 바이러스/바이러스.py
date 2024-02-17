def dfs(num):
    ST = []
    visited = [0]* (N+1) # 방문표시 할 리스트 생성
    ST.append(num)
    visited[num] = 1
    cnt = 0
    while ST: # 스택에 값이 있는 동안 반복
        v = ST.pop(-1)

        for w in G[v]: # 인접리스트 내부의 원소 개수만큼 만큼 반복
            if visited[w] == 0: # 방문하지 않은 곳이면
                ST.append(w)
                visited[w] = 1
                cnt += 1 

    return cnt

import sys
N = int(sys.stdin.readline()) # 컴퓨터의 수 입력받음
pair = int(sys.stdin.readline()) # 쌍의 수

# 인접 리스트 생성
G = [[] for _ in range(N+1)] # 편의를 위해 0번 리스트는 사용 X
for _ in range(pair):
    v1, v2 = map(int, sys.stdin.readline().strip().split())

    # 무향그래프이므로 두 번 append
    G[v1].append(v2)
    G[v2].append(v1)

print(dfs(1)) # 1번 컴퓨터