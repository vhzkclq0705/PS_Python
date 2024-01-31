# Silver 5 - 크로아티아 알파벳

alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()

for alphabet in alphabets:
    s = s.replace(alphabet, '*')

print(len(s))