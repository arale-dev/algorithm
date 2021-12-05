from itertools import combinations
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        answer = 0
        pairs = combinations(range(len(colors)), 2)
        for a,b in pairs:
            if ((b-a) > answer) and colors[a] != colors[b]:
                answer = b-a        
        return answer