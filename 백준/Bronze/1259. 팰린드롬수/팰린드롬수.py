import sys

while True:
    word = sys.stdin.readline().strip()
    if word == '0':
        break
        
    if word == word[::-1]:
        print('yes')
    else:
        print('no')
