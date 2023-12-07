# Bronze 2 - Hashing

n = int(input())
s = input()
total = 0

for i in range(n):
    total += (ord(s[i]) - 96) * (31 ** i)

print(total % 1234567891)