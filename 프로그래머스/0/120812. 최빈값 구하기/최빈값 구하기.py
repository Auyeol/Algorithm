def solution(array):
    array_set = set(array)
    result = []
    for s in array_set:
        result.append((array.count(s), s))
    max_v = max(result)
    cnt = 0
    for r in result:
        if r[0] == max_v[0]:
            cnt += 1
    
    if cnt > 1:
        return -1 
    else:
        return max_v[1]
    