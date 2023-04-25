# LEVEL 2

from itertools import product

def solution(info, query):
    d = dict()
    lan = ['cpp', 'java', 'python', '-']
    dep = ['backend', 'frontend', '-']
    car = ['junior', 'senior', '-']
    foo = ['chicken', 'pizza', '-']
    ans = []
    
    for ll, dd, cc, ff in product(lan, dep, car, foo):
        d[ll+dd+cc+ff] = []
    
    for i in info:
        li, di, ci, fi, score = i.split()
        for ll, dd, cc, ff in product([li, '-'], [di, '-'], [ci, '-'], [fi, '-']):
            d[ll+dd+cc+ff].append(int(score))
    
    for k in d.keys():
        d[k].sort()
    
    for q in query:
        ll, a1, dd, a2, cc, a3, ff, score = q.split()
        tmp = d[ll+dd+cc+ff]
        l = len(tmp)
        s, e = 0, l-1
        
        while s <= e:
            m = (s + e) // 2
            if tmp[m] >= int(score):
                e = m - 1
            else:
                s = m + 1
        ans.append(l - s)
    
    return ans