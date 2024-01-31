# Silver 4 - 숫자 카드 2

from collections import defaultdict
import sys
input = sys.stdin.readline

input()
d = defaultdict(int)
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))

for i in a:
    d[i] += 1

for i in b:
    print(d[i], end=' ')