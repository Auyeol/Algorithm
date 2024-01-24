input_list = list(map(int, input().split()))
normal_list = [1,1,2,2,2,8]
for i in range(len(input_list)):
    input_list[i] = normal_list[i] - input_list[i]
    

print(*input_list)