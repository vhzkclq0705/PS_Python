# Bronze 1 - 팰린드롬수

import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '0':
        break
    print('yes') if n == n[::-1] else print('no')