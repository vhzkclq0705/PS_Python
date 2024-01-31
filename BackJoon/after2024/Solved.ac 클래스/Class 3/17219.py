# Silver 4 - 비밀번호 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()

for _ in range(n):
    address, password = map(str, input().rstrip().split())
    d[address] = password

for _ in range(m):
    print(d[input().rstrip()])