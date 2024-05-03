def solution(numbers):
    my_arr = [0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers:
        my_arr.remove(i)

    return sum(my_arr)