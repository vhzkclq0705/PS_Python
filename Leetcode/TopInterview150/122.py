# 122. Best Time to Buy and Sell Stock 2 - Medium

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
          tmp = prices[i]

          if tmp > min_price:
            max_profit += tmp - min_price
          
          min_price = tmp
        
        return max_profit