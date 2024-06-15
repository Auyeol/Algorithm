def solution(s):
    s_dict = {}
    result = []
    
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
    
    for i in s_dict:
        if s_dict[i] == 1:
            result.append(i)
            
    result.sort()
    return ''.join(result)