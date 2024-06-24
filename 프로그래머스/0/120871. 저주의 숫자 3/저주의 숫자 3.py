def solution(n):
    arr = []
    i = 1
    while len(arr) < n:
        if i%3 != 0 and '3' not in str(i):
            arr.append(i)
        i += 1
        
    return arr[n-1]