# Silver 4 - 수 찾기

import sys
input = sys.stdin.readline

input()
a = set(map(int, input().split()))
input()
b = list(map(int, input().split()))

for i in b:
    print(1 if i in a else 0)