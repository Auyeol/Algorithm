def solution(s):
    if s[0] == '-':
        num = 0 - int(s[1:])
    else:
        num = int(s)
    
    return num