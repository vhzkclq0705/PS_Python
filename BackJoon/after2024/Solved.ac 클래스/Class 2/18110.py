# Silver 4 - solved.ac

import sys
input = sys.stdin.readline

def round(n):
    return int(n) + 1 if n % 1 >= 0.5 else int(n)

n = int(input())
diff = sorted([int(input()) for i in range(n)])
avg = round(n * 0.15)

print(round(sum(diff[avg:n - avg]) / (n - avg * 2)) if n != 0 else 0)