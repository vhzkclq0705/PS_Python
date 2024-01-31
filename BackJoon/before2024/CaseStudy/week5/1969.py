import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(input().rstrip()) for _ in range(n)]
a = ['A', 'C', 'G', 'T']
cnt = [[0] * 4 for _ in range(m)]
ansString = ""
ansCnt = 0

for i in range(n):
    for j in range(m):
        for k in range(4):
            if s[i][j] == a[k]:
                cnt[j][k] += 1

for i in cnt:
    maxValue = max(i)
    for j in range(4):
        if i[j] == maxValue:
            ansString += a[j]
            maxValue = -1
        elif i[j] > 0:
            ansCnt += i[j]

print(ansString)
print(ansCnt)

## 다른 풀이
# n, m = map(int, input().split())

# arr = []

# # 문자열을 list형식으로 담아준다
# for i in range(n):
#     arr.append(list(map(str, input())))

# cnt, hap = 0, 0
# result = ''
# for i in range(m):
#     a, c, g, t = 0, 0, 0, 0
#     for j in range(n):
#         if arr[j][i] == 'T':
#             t += 1
#         elif arr[j][i] == 'A':
#             a += 1
#         elif arr[j][i] == 'G':
#             g += 1
#         elif arr[j][i] == 'C':
#             c += 1
#     if max(a,c,g,t) == a:
#         result += 'A'
#         hap += c + g +t
#     elif max(a,c,g,t) == c:
#         result += 'C'
#         hap += a + g +t
#     elif max(a,c,g,t) == g:
#         result += 'G'
#         hap += a + c +t
#     elif max(a,c,g,t) == t:
#         result += 'T'
#         hap += c + g + a
    
# print(result)
# print(hap)