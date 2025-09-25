from threading import Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cond = Condition()
        self.q = deque()
        # Python condition vs lock vs semaphore vs barrier
        '''
        Lock: Mutual exclusion for shared resource. Call lock.lock() while operating on critical section/shared resource. Then call unlock()
        Condition: wait on some condition, blocked until notify() is called
        Semaphore: Limit concurrent access to n threads at a time (Semaphore(n)), block after n
        Barrier: Blocks until all required threads call wait() - i.e. awaits the state where n number of threads have had a chance to 'line up next to the barrier'
        '''

    def enqueue(self, element: int) -> None:
        with self.cond:
            while len(self.q) == self.cap:
                self.cond.wait()
            self.q.append(element)
            self.cond.notifyAll()

    def dequeue(self) -> int:
        with self.cond:
            while len(self.q) == 0:
                self.cond.wait()
            self.cond.notifyAll()
            return self.q.popleft()

    def size(self) -> int:
        return len(self.q)
