input_str = input()
alpha_list = [-1]*26
alpha = 'abcdefghijklmnopqrstuvwxyz'
idx = 0
for s in input_str:
    if alpha_list[alpha.index(s)]>-1:
        pass
    else:
        alpha_list[alpha.index(s)] = idx
    idx += 1
    

for i in alpha_list:
    print(i, end=' ')