import sys

# 입력 받기
input_string = sys.stdin.readline().strip().upper()

# 각 문자의 개수를 저장할 딕셔너리 생성
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 가장 많이 등장한 문자와 그 등장 횟수 찾기
max_count = max(char_count.values())
max_chars = [char for char, count in char_count.items() if count == max_count]

# 최댓값이 유일한지 확인
if len(max_chars) == 1:
    print(max_chars[0])
else:
    print("?")
