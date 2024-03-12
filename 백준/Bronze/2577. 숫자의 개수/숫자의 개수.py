import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = list(str(A * B * C))

print(result.count('0'))
print(result.count('1'))
print(result.count('2'))
print(result.count('3'))
print(result.count('4'))
print(result.count('5'))
print(result.count('6'))
print(result.count('7'))
print(result.count('8'))
print(result.count('9'))
