from threading import Condition

class FooBar:
    def __init__(self, n):
        self.n = n
        self.cond = Condition()
        self.turn = "foo"

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.cond:
                while self.turn != "foo":
                    self.cond.wait()
                self.turn = "bar"
                self.cond.notifyAll()

                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            with self.cond:
                while self.turn != "bar":
                    self.cond.wait()
                self.turn = "foo"
                self.cond.notifyAll()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
