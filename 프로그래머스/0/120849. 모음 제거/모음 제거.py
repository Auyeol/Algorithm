def solution(my_string):
    aeiou = ['a','e','i','o','u']
    answer = ''
    
    for c in my_string:
        if c not in aeiou:
            answer += c
    
    return answer