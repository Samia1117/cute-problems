class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
        # print(f'after push = {self.stack}')

    # Remove the top element from the stack (no need to return it)
    # [(2,2), (0, 0), (3, 0), (0, 0)]
    # min = 0
    # pop = [(2,2), (0, 0), (3, 0)]
    # min = 0
    def pop(self) -> None:
        self.stack.pop()
        # print(f'after pop = {self.stack}')

    # Return the last added element (at the 'top') in the stack, but don't remove it from the stack ('peek')
    def top(self) -> int:
        # print(f'return top from = {self.stack}')
        return self.stack[-1][0] # deque[-1] = last added, deque[0] = first added

    
    # Return the minimum elt. in the stack, but don't remove it. Should run in O(1) time
    def getMin(self) -> int:
        # print(f'return min from = {self.stack}')
        return self.stack[-1][1] # deque[-1] = last added, deque[0] = first added



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
