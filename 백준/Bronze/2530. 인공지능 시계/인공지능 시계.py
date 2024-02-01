hour, minute, second = map(int, input().split())

input_time = int(input())

second += input_time
minute += second//60
hour += minute//60

print(hour%24, minute%60, second%60)