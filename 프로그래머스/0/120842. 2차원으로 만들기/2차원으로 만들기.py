def solution(num_list, n):
    result = []
    
    for i in range(0, len(num_list), n):
        temp = []
        for j in range(i, i+n):
            temp.append(num_list[j])
        result.append(temp)
    return result