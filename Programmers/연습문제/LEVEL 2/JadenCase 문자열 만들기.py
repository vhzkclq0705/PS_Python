# LEVEL 2

def solution(s):
    ans = ''

    for i in s:
        if not ans or i.isdigit() or i == ' ':
            ans += i.upper()
        else:
            if ans[-1] == ' ' or not ans:
                ans += i.upper()
            else:
                ans += i.lower()

    return ''.join(ans)