# Bronze 1 - 최대공약수와 최소공배수

import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))