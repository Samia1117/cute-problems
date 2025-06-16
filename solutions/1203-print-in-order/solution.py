from threading import Condition

class Foo:
    def __init__(self):
        pass
        self.cv = Condition()
        self.first_happened = False
        self.second_happened = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        with self.cv:
            printFirst()
            self.first_happened = True
            self.cv.notify_all()
            return

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.cv:
            while not self.first_happened:
                self.cv.wait()
            printSecond()
            self.second_happened = True
            self.cv.notify_all()
            return


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.cv:
            while not self.second_happened:
                self.cv.wait()
            printThird()
            return 
