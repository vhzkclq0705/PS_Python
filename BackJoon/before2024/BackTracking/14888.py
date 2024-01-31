# Silver 1 - 연산자 끼워넣기

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
min_Value = 10e9
max_Value = -10e9

def bt(total, i, ops):
    global min_Value
    global max_Value

    if i == n - 1:
        min_Value = min(total, min_Value)
        max_Value = max(total, max_Value)
        return
    
    if ops[0] > 0:
        ops[0] -= 1
        bt(total + nums[i + 1], i + 1, ops)
        ops[0] += 1
    if ops[1] > 0:
        ops[1] -= 1
        bt(total - nums[i + 1], i + 1, ops)
        ops[1] += 1
    if ops[2] > 0:
        ops[2] -= 1
        bt(total * nums[i + 1], i + 1, ops)
        ops[2] += 1
    if ops[3] > 0:
        ops[3] -= 1
        if total < 0:
            temp = -(abs(total) // nums[i + 1])
        else:
            temp = total // nums[i + 1]
        bt(temp, i + 1, ops)
        ops[3] += 1

bt(nums[0], 0, ops)
print(max_Value)
print(min_Value)