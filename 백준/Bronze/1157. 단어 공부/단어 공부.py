import sys
word = sys.stdin.readline().strip().upper()
my_dict = {}
for c in word:
    if c in my_dict:
        my_dict[c] += 1
    else:
        my_dict[c] = 1

max_v = max(my_dict.values())
arr = []
for item in my_dict.items():
    if item[1] == max_v:
        arr.append(item[0])

if len(arr) >= 2:
    print('?')
else:
    print(arr[0])