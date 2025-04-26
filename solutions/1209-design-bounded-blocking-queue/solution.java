// import java.util.package;

class BoundedBlockingQueue {

    private final LinkedList<Integer> queue;
    private final int capacity;
    private Lock lock = new ReentrantLock();
    private final Condition queueEmpty = lock.newCondition();
    private final Condition queueFull = lock.newCondition();
    private int size;

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new LinkedList<>(); 
        /*
        if (queue == null) {
            synchronized(BoundedBlockingQueue.class) {
                if (queue == null) {
                    queue = new LinkedList<>(); // initialize this only once
                }
            }
        }
        **/
    }
    
    public void enqueue(int element) throws InterruptedException {
        lock.lock();
        try {
            while (size == capacity) {
                queueFull.await();
            }
            queue.offer(element);
            size++;
            queueEmpty.signal();
        } finally {
            lock.unlock();
        }

    }
    
    public int dequeue() throws InterruptedException {
        lock.lock();
        try {
            while (size == 0) {
                queueEmpty.await();
            }
            queueFull.signal();
            size--;
            return queue.poll();
        } finally {
            lock.unlock();
        }
    }
    
    public int size() {
        lock.lock();
        try {
            return size;
        } finally {
            lock.unlock();
        }
    }
}
