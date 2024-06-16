def solution(spell, dic):
    result = ''
    answer = 2
    for d in dic:
        for s in spell:
            print(s, list(d))
            if s in list(d):
                continue
            else:
                result += 'n'
        if result == '':
            answer = 1
            result = ''
        result = ''
            
    return answer