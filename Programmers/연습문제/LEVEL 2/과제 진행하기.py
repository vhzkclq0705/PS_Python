# LEVEL 2

def solution(plans):
    plans.sort(key=lambda x:x[1])
    stack = []
    ans = []
    
    for p_sub, p_start, p_left in plans:
        h, m = map(int, p_start.split(':'))
        p_start = h * 60 + m
        p_left = int(p_left)
        
        if stack:
            n_sub, n_start, n_left = stack.pop()
            time = p_start - n_start
            
            if time < n_left:
                stack.append((n_sub, n_start, n_left - time))
            else:
                ans.append(n_sub)
                time -= n_left
                
                while stack and time:
                    n_sub, n_start, n_left = stack.pop()
                    
                    if time < n_left:
                        stack.append((n_sub, n_start, n_left - time))
                        break
                    else:
                        ans.append(n_sub)
                        time -= n_left
        
        stack.append((p_sub, p_start, p_left))
    
    return ans + [stack[i][0] for i in range(len(stack) - 1, -1, -1)]