from threading import RLock
from threading import Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.bq = deque()
        self.current_size = 0
        self.capacity = capacity
        # lock is open to being acquired at initialization
        # self.lock = RLock()
        self.cond = Condition()
        

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        # print("At enqueue\n")
        self.cond.acquire()
        while self.current_size == self.capacity:
            self.cond.wait()

        self.bq.append(element)
        self.current_size += 1

        self.cond.notifyAll()
        self.cond.release()

        # try:
        #     # acquire the lock
        #     self.lock.acquire()

        #     if self.current_size < self.capacity:
        #         # do some work
        #         self.bq.append(element)
        #         self.current_size += 1

        #         # release the lock
        #         self.lock.release()
        # except:
        #     self.lock.release()
        #     pass
        

    def dequeue(self):
        """
        :rtype: int
        """
        # print("At deque\n")

        self.cond.acquire()
        while self.current_size == 0:
            self.cond.wait()
        
        popped = self.bq.popleft()
        self.current_size -= 1

        self.cond.notifyAll()
        self.cond.release()
        return popped

        # try:
        #     # acquire the lock
        #     self.lock.acquire()

        #     if self.current_size > 0:
        #         # do some work
        #         popped = self.bq.popleft()
        #         self.current_size -= 1

        #         # release the lock
        #         self.lock.release()
        #         return popped
        # except:
        #     self.lock.release()
        #     pass
        

    def size(self):
        """
        :rtype: int
        """
        return self.current_size
        
