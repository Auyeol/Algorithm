def solution(sides):
    cnt = 0
    
    # 리스트 내의 수가 가장 긴 변인 경우 
    max_len = max(sides)
    min_len = min(sides)
    
    idx = 1
    while max_len >= idx:
        if idx + min_len > max_len:
            cnt += 1
        idx += 1

    # 리스트 외부의 값이 가장 긴 변인 경우
    # 가장 큰 값보다 합까지
    cnt += (sum(sides) - max_len) 

    return cnt - 1