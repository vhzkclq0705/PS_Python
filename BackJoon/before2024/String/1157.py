# Bonze 1 - 단어 공부

a = [0] * 26
s = input().upper()

for i in s:
    a[ord(i) - 65] += 1

max_value = max(a)
print("?" if a.count(max_value) > 1 else chr(a.index(max_value) + 65))