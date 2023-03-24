# LEVEL 1

def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    for i in s:
        idx = (alphabet.index(i) + index) % len(alphabet)
        answer += str(alphabet[idx])
    
    return answer