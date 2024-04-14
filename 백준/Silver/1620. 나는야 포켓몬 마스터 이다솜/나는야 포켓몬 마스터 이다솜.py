import sys
N, M = map(int, sys.stdin.readline().split())

# N 개의 줄에 포켓몬 번호가 1번 ~ N번 포켓몬이 한 줄에 하나씩 입력으로 들어옴
# 첫 글자만 대문자, 나머지는 소문자 / 마지막 문자만 대문자인 경우 존재
# 포켓몬 이름의 최대 길이는 20, 최소 길이 2
pokemon_dict = {}
pokemon_num_dict = {}   # 시간초과 때문에 num을 저장하는 dict 생성
for i in range(1, N+1):
    pokemon = sys.stdin.readline().strip()
    pokemon_dict[i] = pokemon
    pokemon_num_dict[pokemon] = i
# 그 다음 줄 부터 총 M개의 줄에 맞춰야하는 무제가 입력으로 들어옴
# 알파벳으로 들어오면 포켓몬 번호 말하기
# 숫자로 들어오면 포켓몬 번호에 해당하는 문자 출력
for i in range(M):
    prob = sys.stdin.readline().strip()
    if prob.isdigit():
        print(pokemon_dict[int(prob)])
    else:
        print(pokemon_num_dict[prob])
