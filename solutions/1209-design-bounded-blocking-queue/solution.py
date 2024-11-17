from threading import Condition
from threading import Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = deque()
        self.cap = capacity

        self.cond = Condition()

        self.enq_lock = Lock()
        self.deq_lock = Lock()

        self.deq_lock.acquire()

    def enqueue(self, element: int) -> None:

        self.enq_lock.acquire()
        self.queue.append(element)
        
        if self.deq_lock.locked():
            self.deq_lock.release()
        if len(self.queue) < self.cap:
            self.enq_lock.release()

        # self.cond.acquire()
        # while len(self.queue) == self.cap:
        #     self.cond.wait()
        
        # self.queue.append(element)
        # # print(f'Self.q = {self.queue}')
        # self.cond.notify_all()
        # self.cond.release()

    def dequeue(self) -> int:

        self.deq_lock.acquire()
        elt = self.queue.popleft()

        if self.enq_lock.locked():
            self.enq_lock.release()

        if len(self.queue) > 0:
            self.deq_lock.release()

        return elt

        # self.cond.acquire()
        # while len(self.queue) == 0:
        #     self.cond.wait()

        # elt = self.queue.popleft()  # Note, the elt has already been popped so cannot do anything more about it 
        # # print(f'Self.q = {self.queue}')
        # self.cond.notify_all()
        # self.cond.release()
        # return elt

    def size(self) -> int:
        return len(self.queue)
        
