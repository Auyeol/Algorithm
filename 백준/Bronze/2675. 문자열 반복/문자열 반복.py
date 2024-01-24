case_num = int(input())

for i in range(case_num):
    repeat, input_str = input().split()
    
    for j in input_str:
        print(j*int(repeat), end='')
    print()
    