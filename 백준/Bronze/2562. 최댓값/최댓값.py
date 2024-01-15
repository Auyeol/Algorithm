aList = []
maxNum = 0
idx = 0
while True:
  try:
    a = int(input())
    aList.append(a)
    if(a>maxNum):
      maxNum = a
      idx = aList.index(maxNum) + 1
  except:
    break
print(maxNum)
print(idx)