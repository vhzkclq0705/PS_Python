# LEVEL 2

from collections import Counter

def solution(str1, str2):
    s1 = Counter([str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()])
    s2 = Counter([str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()])
    
    a = sum((s1&s2).values())
    b = sum((s1|s2).values())
    
    return 65536 if b == 0 else int(a / b * 65536)