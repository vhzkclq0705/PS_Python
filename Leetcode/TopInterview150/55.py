# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
      reachable = 0

      for i in range(len(nums)):
        if i > reachable:
          return False
        if reachable >= len(nums) - 1:
          return True
        
        reachable = max(reachable, i + nums[i])