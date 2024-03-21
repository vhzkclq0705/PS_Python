def solution(record):
    answer = []
    msg = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
    d = dict()
    
    for i in record:
        info = i.split()
        if len(info) == 3:
            d[info[1]] = info[2]
    
    for i in record:
        info = i.split()
        if info[0] in msg:
            answer.append(d[info[1]] + '님이 ' + msg[info[0]])
            
    return answer