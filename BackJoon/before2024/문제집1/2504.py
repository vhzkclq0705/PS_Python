# silver 1 - 괄호의 값

def check(s):
    if s.count('(') != s.count(')') or s.count('[') != s.count(']'):
        return False
    
    while s:
        tmp = s
        s = s.replace('()', '').replace('[]', '')
        if tmp == s:
            return False
    
    return True

def solution(s):
    if not check(s):
        return 0
    
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                tmp = 0
                for j in range(len(stack)-1, -1, -1):
                    if type(stack[j]) == int:
                        tmp += stack[j]
                        stack.pop()
                    elif stack[j] == '(':
                        stack.pop()
                        break
                stack.append(tmp * 2)
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                tmp = 0
                for j in range(len(stack)-1, -1, -1):
                    if type(stack[j]) == int:
                        tmp += stack[j]
                        stack.pop()
                    elif stack[j] == '[':
                        stack.pop()
                        break
                stack.append(tmp * 3)
                
    return sum(stack)

print(solution(input()))