class MinStack:

    def __init__(self):
        self.min_vals = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        
        # if (len(self.min_vals) == 0):
        #     self.min_vals.append(val)
        # elif (self.min_vals[-1] > val ):
        #     self.min_vals.append(val)
        # else:
        #     self.min_vals.append(self.min_vals[-1])
        
        self.stack.append(val)
        val = min(val, self.min_vals[-1] if self.min_vals else val)
        self.min_vals.append(val)
        

    def pop(self) -> None:
        
        if (len(self.min_vals) !=0):
            self.min_vals.pop()
        
        self.stack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.min_vals[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
