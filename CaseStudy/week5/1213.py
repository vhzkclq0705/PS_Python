import sys
input = sys.stdin.readline

s = input().rstrip()
a = [0] * 26
cnt = 0
ans = ""
center = ""

for i in s:
    a[ord(i) - ord('A')] += 1

for i in range(26):
    if a[i] % 2 == 1:
        cnt += 1
        center += chr(i + ord('A'))
    if cnt == 2:
        print("I'm Sorry Hansoo")
        exit()
    ans += chr(i + ord('A')) * (a[i] // 2)

print(ans + center + ans[::-1])