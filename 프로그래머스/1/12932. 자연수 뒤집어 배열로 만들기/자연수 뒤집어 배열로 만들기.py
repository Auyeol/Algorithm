def solution(n):
    result = []
    
    s = str(n)

    
    for i in range(len(s)-1, -1, -1):
        result.append(int(s[i]))
    return result