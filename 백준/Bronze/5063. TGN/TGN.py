T = int(input())

for tc in range(1, T+1):
    R, E, C = map(int, input().split())

    if R < E - C:
        print('advertise')
    elif R == E - C:
        print('does not matter')
    else:
        print('do not advertise')