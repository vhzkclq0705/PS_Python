# Silver 2 - 좌표 압축

int(input())
nums = list(map(int, input().split()))
set_nums = sorted(set(nums))
dict = {}

for i in range(len(set_nums)):
    dict[set_nums[i]] = i 

for num in nums:
    print(dict[num], end=' ')