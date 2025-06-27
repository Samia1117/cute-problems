from threading import Lock
from threading import Condition
from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

        self.odd_lock = Semaphore()
        self.even_lock = Semaphore()
        self.zero_lock = Semaphore()

        self.count = 1

        self.odd_lock.acquire()
        self.even_lock.acquire()

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        
        # while self.count < self.n:
        for _ in range(self.n):
            self.zero_lock.acquire()

            printNumber(0)

            if self.count % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        
            for _ in range(2, self.n + 1, 2):
            # while self.count < self.n:
                self.even_lock.acquire()

                printNumber(self.count)
                self.count += 1

                self.zero_lock.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:

            for _ in range(1, self.n + 1, 2):
            # while self.count < self.n:
                self.odd_lock.acquire()

                printNumber(self.count)
                self.count += 1

                self.zero_lock.release()
        
