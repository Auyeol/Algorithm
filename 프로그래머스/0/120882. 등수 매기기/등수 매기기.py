def solution(score):
    avg_lst = []
    result = []
    
    for s in score:
        avg_lst.append(sum(s)/2)
    
    avg_sort = sorted(avg_lst, reverse=True)
    
    for avg in avg_lst:
        result.append(avg_sort.index(avg) + 1)
    
    print(avg_lst)
    print(avg_sort)
    print(result)
    return result
        
    