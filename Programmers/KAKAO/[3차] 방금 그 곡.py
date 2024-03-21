# LEVEL 2

def solution(m, musicinfos):
    def divide_str(s):
        tmp = []
        for i in s:
            if i == '#':
                tmp[-1] += i
            else:
                tmp.append(i)
        return tmp
    
    answer = []
    m = divide_str(m)
    
    for music in musicinfos:
        start, end, title, m_s = music.split(',')
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        time = end - start
        m_s = divide_str(m_s)
        
        a, b = divmod(time, len(m_s))
        res = m_s * a + m_s[:b]
        p, cnt = 0, 0
        lm = len(m)

        while p <= len(res) - lm:
            if res[p:p + lm] == m:
                cnt += 1
                p += lm
            else:
                p += 1
        
        if cnt:
            answer.append((cnt, time, start, title))
        
    return sorted(answer, key=lambda x:(-x[0], -x[1], x[2]))[0][-1] if answer else '(None)'