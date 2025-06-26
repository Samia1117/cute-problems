from threading import Semaphore
from threading import Lock

class DiningPhilosophers:
    # make a map of philosopher_id: [lock_for_left_fork, lock_for_right_fork]
    # note left and right fork are both shared by two other philosophers
    # so maybe makes sense to have a dictionary: {lock: [philosopher_1, philosopher_2]}
    #  --- each object (fork) is shared by two philosophers
    #  -------- when one philosopher finishes eating (finishes eat() function), it can notify the other philosopher, and can release that lock
    # Let's be concrete: p1 has rlock with id1. p2 has leftlock with id1. p1 has leftlock with id0 (or x, s.t. x%n == 0, where n is # philosophers).
    # similarly, p2 has rlock with id2, p3 has leftlock with id2. p3 should have right lock = id0, but it becomes id3. 
    # ----- how do I ensure that id3 = id0?
    # Answer: IT'S GIVEN!!!!!

    # call the functions directly to execute, for example, eat()

    def __init__(self):
        self.lock_arr = [Lock() for _ in range(5)]
        self.concurr_limit_lock = Semaphore(4)

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        # each philosopher will grab philosopher, (philosopher + 1) %5 indexed entry in lock_arr
        llock, rlock = self.lock_arr[philosopher], self.lock_arr[(philosopher + 1) % 5]
        # print(f'llock, rlock = {str(llock)}, {str(rlock)}')

        with self.concurr_limit_lock:
            with llock, rlock:
                pickLeftFork()
                pickRightFork()
                # print(f'Philosopher {philosopher} is about to eat..')
                eat()
                putLeftFork()
                putRightFork()
                    
        
