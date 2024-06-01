def solution(n):
    cnt = 0
    result = []
    while cnt <= n:
        if cnt % 2 == 1:
            result.append(cnt)
        cnt += 1
    return result 
