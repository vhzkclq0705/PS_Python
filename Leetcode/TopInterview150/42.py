# 42. Trapping Rain Water - Hard

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[0], height[-1]

        while left < right:
          max_left = max(max_left, height[left])
          max_right = max(max_right, height[right])

          if max_left <= max_right:
            water += max_left - height[left]
            left += 1
          else:
            water += max_right - height[right]
            right -= 1

        return water