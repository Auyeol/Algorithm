T = int(input())

one = 0
zero = 0
    
    
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        one += 1
    else:
        zero += 1
        
if one > zero:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
