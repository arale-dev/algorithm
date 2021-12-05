from collections import deque, defaultdict

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        answer = ''
        info = defaultdict()
        for idx, value in enumerate(cost):
            info[value] = (idx + 1)
            
        @cache
        def fn(remain_cost):
            if remain_cost == 0:
                return 0
            elif remain_cost > 0:
                return max(fn(remain_cost-k)* 10 + info[k] for k in info)
            else:
                return -5001
        
        return str(max(fn(target), 0))