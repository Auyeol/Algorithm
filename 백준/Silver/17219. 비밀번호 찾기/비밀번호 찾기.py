import sys

N, M = map(int, sys.stdin.readline().strip().split())
password_dict = {}
for _ in range(N):
    site, pwd = sys.stdin.readline().strip().split()
    password_dict[site] = pwd

for _ in range(M):
    find_pwd = sys.stdin.readline().strip()
    print(password_dict[find_pwd])