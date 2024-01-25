case_num = int(input())
sum = 0
for i in range(case_num):
    input_str = input()
    cnt = 0
    for elem in input_str: 
        if(elem == 'O'):
            cnt +=1 
            sum += cnt 
        if(elem=='X'): 
            cnt = 0
    print(sum) 
    sum = 0 