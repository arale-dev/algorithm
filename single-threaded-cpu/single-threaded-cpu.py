import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        self.answer = []
        
        tasks = list(enumerate(tasks))
        tasks.sort(key = lambda x: x[1][0])
        
        self.heap = []
        self.clock = 0
        
        for task in tasks:
            i, [enqueT, processingT] = task
            if self.clock <= enqueT:
                while self.clock < enqueT and self.heap:
                    self.getNextProcess()
            if self.clock <= enqueT and not self.heap:
                self.clock = enqueT
            heapq.heappush(self.heap, (processingT, i))
                    
        while self.heap:
            self.getNextProcess()
        
        return self.answer
    
    def getNextProcess(self):
        processingT, idx = heapq.heappop(self.heap)
        self.clock += processingT
        self.answer.append(idx)