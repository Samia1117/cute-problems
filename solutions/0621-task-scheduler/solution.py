import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        def updateQueues(ready_queue, cooldown_queue, wait_time_decrement_offset):
            
            # Updated cooldown_queue to return
            new_cooldown_queue = []
            heapq.heapify(new_cooldown_queue)

            # Check if any task in cooldown_queue is ready to be put into ready_queue
            while cooldown_queue:
                # Pop each task and inspect if it is ready for execution
                task = cooldown_queue.pop()
                # Decrement the effect of this execution cycle (***)
                task.wait_time -= wait_time_decrement_offset

                # If task has waited long enough, move it to ready state
                if task.wait_time <= 0:
                    heapq.heappush(ready_queue, Task(task.label, task.count, task.wait_time))   
                # Otherwise, return it to cooldown_queue for it to cooldown for longer
                else:
                    heapq.heappush(new_cooldown_queue, task)

            return new_cooldown_queue

        '''
        Task obj with two attributes: 
        `count` -> number of instances of this Task type
        `wait_time` -> time this Task needs to wait before it can be scheduled for execution
        '''
        class Task:
            def __init__(self, label, count, wait_time):
                self.label = label
                self.count = count
                self.wait_time = wait_time

            def __lt__(self, other):
                return self.count > other.count  # For max heap
            
            def __repr__(self):
               return f" {self.label} {self.count} {self.wait_time} "

        '''
        Like 'Task' but its __lt__ operator can build a min heap based on `wait_time`
        '''
        class StalledTask:
            def __init__(self, label, count, wait_time):
                self.label = label
                self.count = count
                self.wait_time = wait_time

            def __lt__(self, other):
                return self.wait_time < other.wait_time  # For min heap
            
            def __repr__(self):
               return f"Stalledtask {self.label} {self.count} {self.wait_time} "

        # Create a Hashmap of the form: {"A":[count, wait_time], "B":[], ..}
        # For any given task, if wait_time <= 0, then this task is ready for execution
        hmap = {}
        for task in tasks:
            if task not in hmap:
                hmap[task] = [0, 0]
            hmap[task][0] += 1

        tasks_count = sum([v[0] for k,v in hmap.items()])

        # build a 'ready_queue' for tasks that are ready for execution
        ready_queue = [Task(item[0], item[1][0], item[1][1]) for item in hmap.items()]
        # prioritize tasks in ready_queue by the frequency of that task remaining
        heapq.heapify(ready_queue)

        # build a 'cooldown_queue' to queue tasks that are not yet ready for execution
        cooldown_queue = []
        heapq.heapify(cooldown_queue)

        idle_cycles = 0
        active_cycles = 0
        while ready_queue or cooldown_queue:
            if ready_queue:
                # Execute the task by popping it off the queue
                task = heapq.heappop(ready_queue)
                # Decrement how many instances of this is/task are remaining
                task.count -= 1 

                # task completed, was an active cycle
                active_cycles += 1

                # If not done with task for good, enqueue it back
                if task.count > 0: 
                    # Reset the time this task needs to wait
                    task.wait_time = n + 1  # To understand why n+1 and not n, see (***)
                    heapq.heappush(cooldown_queue, StalledTask(task.label, task.count, task.wait_time))
                # Else, good to remove this task from the heap for good
                # Decrease the wait_time of all tasks by 1
                cooldown_queue = updateQueues(ready_queue, cooldown_queue, 1)
            else:
                # No task is ready! 
                # We don't want to keep looping until the first instant when a task is ready - so zoom past such idle cycles to such an instant

                # number of cycles until first task is ready
                max_wait_time = cooldown_queue[0].wait_time # recall heap is sorted by min wait_time
                idle_cycles += max_wait_time
                cooldown_queue = updateQueues(ready_queue, cooldown_queue, max_wait_time)

        return active_cycles + idle_cycles


        
