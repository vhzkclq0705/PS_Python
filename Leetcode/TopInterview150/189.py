# 189. Rotate Array - Medium

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        c = dict(Counter(nums))
        
        return max(c, key = lambda x: c[x])