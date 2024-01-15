a, b = map(int, input().split())
aList = map(int, input().split())
answer_list = []
for i in aList:
  if(i<b):
    answer_list.append(i)
  
for i in answer_list:
  print(i, end=' ')