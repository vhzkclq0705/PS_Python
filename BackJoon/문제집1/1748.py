# Silver 4 - 수 이어 쓰기 1

n = int(input())
l = len(str(n))
ans = 0

for i in range(1, l):
    ans += 9*10**(i-1)*i
ans += (n-(10**(l-1))+1)*l
print(ans)