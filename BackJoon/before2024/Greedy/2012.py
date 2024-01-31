# Silver - 3

# 개선 코드 (enumerate 사용)
import sys
input = sys.stdin.readline
print(sum([abs(i+1-a) for i, a in enumerate(sorted([int(input()) for _ in range(int(input()))]))]))

# 기존 코드
import sys
input = sys.stdin.readline

n = int(input())
rank_a = sorted([int(input()) for _ in range(n)])
rank_b = [i for i in range(1, n+1)]
ans = 0

for i in range(n):
    if rank_a != rank_b:
        ans += abs(rank_a[i]-rank_b[i])

print(ans)