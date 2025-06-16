from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.curr = 1
        self.cv = Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        
        while True:
            with self.cv:
                if self.curr > self.n:
                    self.cv.notify_all()    
                    return
                while (self.curr % 3 != 0 or self.curr % 5 == 0):
                    self.cv.wait()
                    if self.curr > self.n:
                        self.cv.notify_all()
                        return

                printFizz()
                self.curr += 1
                self.cv.notify_all()    

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                if self.curr > self.n:
                    self.cv.notify_all()    
                    return
                while (self.curr % 5 != 0 or self.curr % 3 == 0):
                    self.cv.wait()
                    if self.curr > self.n:
                        self.cv.notify_all()
                        return

                printBuzz()
                self.curr += 1 
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                if self.curr > self.n:
                    self.cv.notify_all()    
                    return
                while (self.curr % 5 != 0 or self.curr % 3 != 0):
                    self.cv.wait()
                    if self.curr > self.n:
                        self.cv.notify_all()
                        return

                printFizzBuzz()
                self.curr += 1 
                self.cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.cv:
                if self.curr > self.n:
                    self.cv.notify_all()    
                    return
                while (self.curr % 5 == 0 or self.curr % 3 == 0):
                    self.cv.wait()
                    if self.curr > self.n:
                        self.cv.notify_all()
                        return

                printNumber(self.curr)
                self.curr += 1 
                self.cv.notify_all()
