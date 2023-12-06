# 45. Jump Game 2 - Medium

class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt, end, reachable = 0, 0, 0

        for i in range(len(nums) - 1):
            reachable = max(reachable, i + nums[i])

            if reachable >= len(nums) - 1:
                cnt += 1
                return cnt
            if i == end:
                cnt += 1
                end = reachable
        return cnt