# LEVEL 2

def solution(files):
    tmp = []
    
    for i in range(len(files)):
        head = ''
        number = ''

        for j in files[i].upper():
            if '0' <= j <= '9':
                number += j
            else:
                if number:
                    break
                else:
                    head += j
        
        tmp.append((head, int(number), i, files[i]))
    
    return [i[-1] for i in sorted(tmp, key=lambda x:(x[0], x[1], x[2]))]