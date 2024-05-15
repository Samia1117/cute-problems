from threading import Condition
from threading import RLock

class BoundedBlockingQueue(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.bq = deque()
        self.current_size = 0
        self.capacity = capacity

        # lock is open to being acquired at initialization
        self.q_empty = Condition()
        self.q_full = Condition()
        # self.rlock = RLock()

        self.cv = Condition()

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        with self.cv:
            while self.current_size == self.capacity:
                # self.q_full.wait()
                self.cv.wait()

            self.cv.acquire()

            # do some work
            if self.current_size < self.capacity:
                self.bq.append(element)
                self.current_size += 1

            self.cv.notify()
            self.cv.release()

        # release the threads who are waiting for q to be not empty
        

    def dequeue(self):
        """
        :rtype: int
        """
        # acquire the lock for ensuring q is not empty

        # self.rlock.acquire()
        with self.cv:
            while self.current_size == 0:
                # self.q_empty.wait()
                self.cv.wait()

            # self.cv.acquire()
            print("Has lock?: ", self.cv.acquire())
            popped = self.bq.popleft()
            self.current_size -= 1

            # self.q_full.notify()
            self.cv.notify()
            self.cv.release()

        # self.q_not_empty.acquire()
        # do some work 
        # popped = self.bq.popleft()
        # self.current_size -= 1

        # release the lock for threads waiting on q not to be full
        # self.q_full.notify_all()
        # self.q_empty.notify_all()

        # self.q_not_empty.release()
        # self.rlock.release()
        return popped

        '''The while loop checking for the application’s condition is necessary because wait() can return after an arbitrary long time, and the condition which prompted the notify() call may no longer hold true. '''

    def size(self):
        """
        :rtype: int
        """
        return self.current_size
        
