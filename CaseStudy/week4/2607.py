import sys
input = sys.stdin.readline

n = int(input())
w = [[0] * 26 for _ in range(n)]
ans = 0

for i in range(n):
    s = input().rstrip()
    
    for j in s:
        w[i][ord(j) - ord('A')] += 1

for word in w[1:]:
    plus, minus = 0, 0

    for i in range(26):
        if word[i] > w[0][i]:
            plus += word[i] - w[0][i]
        else:
            minus += w[0][i] - word[i]
    
    if plus < 2 and minus < 2:
        ans += 1

print(ans)