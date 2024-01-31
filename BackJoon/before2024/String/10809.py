# Bronze 5 - 알파벳 찾기

s = input()
for i in range(26):
    print(s.find(chr(i + 97)), end = " ")