basket, case_num = list(map(int, input().split()))
aList = []
for i in range(basket):
    aList.append(i+1)

for i in range(case_num):
    first, end = list(map(int, input().split()))
    aList[first-1:end] = aList[first-1:end][::-1]
    
for i in aList:
    print(i, end=' ')