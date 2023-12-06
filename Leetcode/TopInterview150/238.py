# 238. Product of Array Except Self - Medium

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = []
        cnt_zero = nums.count(0)
        total = 1

        for i in nums:
            if i != 0:
                total *= i

        if cnt_zero > 1:
            return [0] * len(nums)
        elif cnt_zero == 1:
            idx_zero = nums.index(0)
        
            for i in range(len(nums)):
                if i == idx_zero:
                    new.append(total)
                else:
                    new.append(0)
        else:
            for i in nums:
                new.append(total // i)
        
        return new