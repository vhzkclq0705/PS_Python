# Bronze 1 - 단어 공부

word = input().upper()
cnt = [0] * 26

for i in word:
    cnt[ord(i) - 65] += 1

print('?' if cnt.count(max(cnt)) > 1 else chr(cnt.index(max(cnt)) + 65))