# Silver 4 - 알바생 강호

import sys
input = sys.stdin.readline

n = int(input())
people = sorted([int(input()) for _ in range(n)], reverse=True)
print(sum([people[i] - i for i in range(n) if people[i] - i > 0]))