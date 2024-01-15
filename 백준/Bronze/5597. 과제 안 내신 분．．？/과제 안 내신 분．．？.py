aList = [0]*30
answerList = []
idx = 0
for _ in range(28):
  stuNum = int(input())
  aList[stuNum-1] += 1

for i in range(30):
  if(aList[i]== 0):
    answerList.append(i+1)

for i in answerList:
  print(i)