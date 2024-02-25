# 괄호
import sys
# 다음 '('가 나타날 때 까지 pop(), 최종적으로 값이 남아있는 경우가 있다면 NO
def is_valid(s):
    if len(s) % 2 != 0:
        print('NO')
        return

    ST = []

    for c in s:
        if c == '(':  # 여는괄호면 append
            ST.append(c)
        else:  # 닫는괄호면 pop()
            if len(ST) == 0:
                print('NO')
                return
            ST.pop()

    if len(ST) != 0:
        print('NO')
        return
    print('YES')
    return


T = int(sys.stdin.readline())    # 입력 데이터의 수를 나타내는 정수 T가 주어진다

for _ in range(T):
    s = list(sys.stdin.readline().strip())  # 문자열을 입력받은 뒤, 리스트로 변환
    is_valid(s)



