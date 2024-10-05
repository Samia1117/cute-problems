import heapq

class Node(object):
    def __init__(self, val: List[int]):
        self.val = val

    def __repr__(self):
        return f"Node val = {self.val}"

    def __lt__(self, other):
        '''compare nodes based on second attribute a.k.a task processing time'''
        if self.val[1] == other.val[1]:
            return self.val[2] < other.val[2]
        return self.val[1] < other.val[1]

class Solution:

    class Node(object):
        def __init__(self, val: List[int]):
            self.val = val

        def __repr__(self):
            return f"Node = {self.val}"

        # pop Node based on min processing time, at index 1
        def __lt__(self, other):
            return self.val[1] < other.val[1]

    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        if not tasks:
            return []
        if len(tasks) == 1:
            return [0]

        # add an index to each task for keeping track of original order
        tasks_with_index = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        n = len(tasks)
        # sort by enqueue time as CPU has to start on task that is available first
        tasks_sorted = sorted(tasks_with_index, key=lambda x: x[1])
        tasks_sorted = sorted(tasks_sorted, key=lambda x:x[0])
        #print("Sorted tasks: ", tasks_sorted)

        pending_tasks = [Node(tasks_sorted[0])]
        heapq.heapify(pending_tasks)

        #print(f"Pending tasks heap = {pending_tasks}")
        #end_of_time = tasks_sorted[-1][0]
        current_time = tasks_sorted[0][0]
        #print(f"Start time = {current_time}")

        queue_index = 1 # we already have started one task so queue starts at 1, not at 0
        completed_tasks = []
        while pending_tasks:
            completed_task = heapq.heappop(pending_tasks)
            completed_tasks.append(completed_task.val)
            #print(f"Completed task with min processing time = {completed_task.val}")

            current_time += completed_task.val[1] # add the processing time
            #print(f"Updated current time = {current_time}")

            # Add in all tasks to heapq whose enqueue time <= current_time
            # Keep track of the index of last task that was queued
            # print(f'queue index = {queue_index}')
            while queue_index < n and tasks_sorted[queue_index][0] <= current_time:
                next_task = tasks_sorted[queue_index]
                heapq.heappush(pending_tasks, Node(next_task))
                #print(f"Pushed task={next_task} at queue_index={queue_index}")
                queue_index += 1
            
            if not pending_tasks and queue_index < n:
                # CPU idle, zoom forward to the future time the next queued task is supposed to start
                next_task = tasks_sorted[queue_index]
                current_time = next_task[0]
                # add that task to the queue
                heapq.heappush(pending_tasks, Node(next_task))
                queue_index += 1


        #print(f"Completed tasks in order = {completed_tasks}")
        return [x[2] for x in completed_tasks]
        
