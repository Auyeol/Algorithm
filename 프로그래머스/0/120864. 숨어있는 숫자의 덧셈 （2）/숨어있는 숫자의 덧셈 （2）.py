def solution(my_string):
    answer = 0
    
    for c in my_string:
        if c.isalpha():
            my_string = my_string.replace(c, ' ')
    
    arr = map(int, my_string.split())
    return sum(arr)