class MyQueue(object):

    def __init__(self):
        # self.q = []
        self.q = deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # self.q.append(x)
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # return self.q.pop(0)
        return self.q.popleft()

    def peek(self):
        """
        :rtype: int
        """
        # if len(self.q) != 0:
        #     return self.q[0]
        if self.q:
            return self.q[0]
        return None

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
