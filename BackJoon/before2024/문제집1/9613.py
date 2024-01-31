# Silver 4 - GCD 합

from itertools import combinations
from math import gcd
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = list(map(int, input().split()))
    print(sum([gcd(a, b) for a, b in combinations(s[1:], 2)]))