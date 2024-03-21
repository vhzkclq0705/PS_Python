# LEVEL 2

def solution(msg):
    answer = []
    d = {chr(i):i - 64 for i in range(65, 91)}
    n = len(msg)
    i = 0
    
    while i < n:
        w = msg[i]
        for j in range(i + 1, n):
            c = msg[j]
            print(w, c)
            
            if w + c not in d:
                d[w + c] = len(d) + 1
                answer.append(d[w])
                break
            else:
                w += c
                i += 1
        i += 1

    answer.append(d[w])
    return answer