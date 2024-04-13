from collections import deque
T = int(input())    # 테스트케이스 입력 받음

for _ in range(T):  # 테스트케이스만큼 반복
    # 문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서가 몇 번째에 위치한지 M
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = max(arr)
    Q = deque()
    result = []
    cnt = 0
    for i in range(len(arr)):
        Q.append((arr[i], i))

    while Q:
        max_v = max(Q)

        doc_print = Q.popleft()

        if doc_print[0] < max_v[0]:
            Q.append(doc_print)
        else:
            cnt += 1
            if doc_print[1] == M:
                break
            result.append(doc_print)

    print(cnt)