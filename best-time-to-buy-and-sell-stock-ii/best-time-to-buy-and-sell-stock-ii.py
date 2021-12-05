class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        low, high = prices[0], prices[0]
        
        # 편차 리스트
        diff = []
        for i in range(len(prices)-1):
            diff.append(prices[i+1] - prices[i])
            
        # 변곡점마다 사고팔기
        old_grad = 0
        for i in range(len(prices)-1):
            if (old_grad > 0 and diff[i] > 0) or (old_grad == 0 and diff[i] == 0) or (old_grad < 0 and diff[i] < 0):
                continue
            if old_grad == 0:
                if diff[i] > 0:
                    low = prices[i]
            elif old_grad > 0:
                answer += prices[i] - low
            else:
                low = prices[i]
            old_grad = diff[i]
        
        if len(prices) >= 2 and prices[-1] > prices[-2]:
            answer += prices[-1] - low
        
        return answer