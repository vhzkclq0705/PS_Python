# Silver 2 - 잃어버린 괄호

import sys
input = sys.stdin.readline

s = list(input().rstrip().split('-'))
ans = [sum(map(int, i.split('+'))) for i in s]

print(ans[0] - sum(ans[1:]))