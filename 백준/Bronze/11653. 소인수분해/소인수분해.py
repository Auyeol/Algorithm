N = int(input())

if N == 1:
    pass
div_num = 2

while N // div_num > 0:
    if N % div_num == 0:
        print(div_num)
        N //= div_num
    else:
        div_num += 1