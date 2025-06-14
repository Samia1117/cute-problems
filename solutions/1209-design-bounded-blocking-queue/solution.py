from threading import Condition

class BoundedBlockingQueue(object):

    # BoundedBlockingQueue b = BoundedBlockingQueue()
    # b.enqueue(0)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.cond = Condition()
        self.cond = Condition()
        
    def enqueue(self, element: int) -> None: 
        with self.cond: # only enqueue if queue not full
            # print("acquired cond (enqueue)")
            while len(self.queue) >= self.capacity:
                self.cond.wait()
            self.queue.append(element)
            self.cond.notifyAll()

    def dequeue(self) -> int:
        with self.cond: # only deque if queue empty
            # print("acquired cond (dequeue)")
            while len(self.queue) == 0:
                self.cond.wait()
            ans = self.queue.popleft()
            self.cond.notifyAll()
        return ans

    def size(self) -> int:
        return len(self.queue)
        
