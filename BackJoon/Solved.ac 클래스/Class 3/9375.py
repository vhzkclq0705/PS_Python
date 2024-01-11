# Silver 3 - 패션왕 신해빈

import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = []
    ans = 1

    for _ in range(int(input())):
        s = input().split()[1]
        clothes.append(s)
    
    clothes = Counter(clothes)
    for v in clothes.keys():
        ans *= clothes[v] + 1
    
    print(ans - 1)