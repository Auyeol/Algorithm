num_1, num_2 = input().split()
num_1 = num_1[::-1]
num_2 = num_2[::-1]
if(int(num_1)>int(num_2)):
    print(int(num_1))
else:
    print(int(num_2))