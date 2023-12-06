# 26. Remove Duplicates from Sorted Array - Easy

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ''' failed -> Why?
        nums = sorted(list(set(nums)))
        return len(nums)
        '''
        s = set()
        idx = 0

        for i in nums:
            if i not in s:
                nums[idx] = i
                idx += 1
                s.add(i)

        return idx