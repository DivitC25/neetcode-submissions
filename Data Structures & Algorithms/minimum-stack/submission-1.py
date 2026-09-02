class MinStack:

    def __init__(self):
        self.currMin = float('inf')
        self.stack = []
        self.minTillNow = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.currMin = min(self.currMin, val)
        self.minTillNow.append(self.currMin)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minTillNow.pop()
        if len(self.minTillNow) > 0:
            self.currMin = self.minTillNow[-1]
        else:
            self.currMin = float('inf')
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.currMin
        
