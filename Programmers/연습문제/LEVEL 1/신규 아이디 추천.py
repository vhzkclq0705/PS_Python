# LEVEL 1

def solution(new_id):
    ans = ''
    new_id = new_id.lower()
    for i in new_id:
        if i in [str(i) for i in range(10)] + [chr(i) for i in range(97, 123)] + ['-', '_', '.']:
            if ans and ans[-1] == '.' and i == '.':
                continue
            ans += i
    ans = ans.strip('.')
    if len(ans) == 0:
        ans = 'a'
    if len(ans) >= 16:
        ans = ans[:15].strip('.')
    if len(ans) <= 2:
        ans += (3 - len(ans)) * ans[-1]
    return ans