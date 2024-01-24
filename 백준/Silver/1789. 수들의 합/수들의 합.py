num = int(input())
sum = 0
n = 1
while True:
    sum += n
    n += 1
    if (n*(n+1)/2)>num:
        break
print(n-1)