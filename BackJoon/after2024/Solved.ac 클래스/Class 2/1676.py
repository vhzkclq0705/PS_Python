# Silver 5 - 팩토리얼 0의 개수

import math

s = list(str(math.factorial(int(input()))))
cnt = 0

for i in range(len(s) - 1, -1, -1):
    if s[i] != '0':
        print(cnt)
        break
    else:
        cnt += 1