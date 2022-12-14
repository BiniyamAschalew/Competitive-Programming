class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,profit = (0, 0)
        for i in range(len(prices)):
            if prices[i] < prices[left]:
                left = i
            elif prices[i] - prices[left] > profit:
                profit = prices[i] - prices[left]
        return profit
        
        