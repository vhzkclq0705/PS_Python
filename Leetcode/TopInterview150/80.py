# 80. Remove Duplicates from Sorted Araay 2 - Medium

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        idx = 0

        for i in range(len(nums)):
            if d[nums[i]] < 2:
                d[nums[i]] += 1
                nums[idx] = nums[i]
                idx += 1
        
        return idx