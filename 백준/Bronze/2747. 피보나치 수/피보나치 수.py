import sys

num = int(sys.stdin.readline())
aList = [0,1]

for i in range(num):
    aList.append(aList[-1]+aList[-2])

print(aList[num])