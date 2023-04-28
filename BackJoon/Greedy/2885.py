# Silver 2 - 초콜릿 식사

import sys
input = sys.stdin.readline

k = int(input())
bin_k = bin(k)[2:]

if bin_k[0] == '1' and bin_k.count('1') == 1:
    print(k, 0)
else:
    size = int('1'+'0'*len(bin_k), 2)
    tmp = size
    cnt = 0

    while k:
        if k >= tmp:
            k -= tmp
        else:
            tmp //= 2
            cnt += 1
    
    print(size, cnt)