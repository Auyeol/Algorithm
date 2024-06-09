def solution(n):
    i = 1
    while True:
        if (n * i) % 6 == 0:
            return (n*i)//6
        i += 1