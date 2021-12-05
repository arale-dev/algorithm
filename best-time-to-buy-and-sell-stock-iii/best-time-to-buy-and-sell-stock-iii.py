class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost_t1, profit_t1 = prices[0], 0
        cost_t2, profit_t2 = prices[0], 0
        
        for price in prices:
            cost_t1 = min(cost_t1, price)
            profit_t1 = max(profit_t1, price - cost_t1)
            cost_t2 = min(cost_t2, price - profit_t1)
            profit_t2 = max(profit_t2, price - cost_t2)
        
        return profit_t2