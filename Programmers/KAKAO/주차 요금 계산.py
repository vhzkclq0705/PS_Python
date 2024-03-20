# LEVEL 2

from collections import defaultdict
import math

def solution(fees, records):
    d = defaultdict(list)
    time = defaultdict(int)
    ans = []
    
    for i in records:
        r = i.split()
        t = int(r[0][:2]) * 60 + int(r[0][3:])
        n = r[1]
        s = r[2]
        
        d[n].append(t)
    
    for k, v in d.items():
        if len(v) % 2 != 0:
            d[k].append(1439)
        
        for i in range(len(v) - 1, 0, -2):
            time[k] += v[i] - v[i - 1]
    
    for k, v in sorted(time.items()):
        if v <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + (math.ceil((v - fees[0]) / fees[2])) * fees[3]
        ans.append(fee)
    
    return ans