class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer, min_price = 0, sys.maxsize
        
        for curr_price in prices:
            min_price = min(min_price, curr_price)
            answer = max(answer, curr_price - min_price)
            
        return answer