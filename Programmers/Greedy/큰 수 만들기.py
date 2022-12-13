# LEVEL 2

def solution(number, k):
    ans = []
    
    for num in number:
        while k > 0 and ans and ans[-1] < num:
            ans.pop()
            k -= 1
        ans.append(num)

    return "".join(ans[:len(number) - k])

number = "1924"
k = 2
print(solution(number, k))

number = "1231234"
k = 3
print(solution(number, k))

number = "4177252841"
k = 4
print(solution(number, k))