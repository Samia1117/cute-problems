# from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Task:
    task_id: int
    task_description: str
    due_date: int
    tags: list[str]
    is_complete: bool = False

    def __lt__(self, other: "Task") -> bool:
        return self.due_date < other.due_date

from sortedcontainers import SortedList as BST
from collections import defaultdict

class TodoList:

    def __init__(self):
        # self.user_to_task_map = defaultdict(list)
        self.user_to_task_map = defaultdict(BST)
        self.counter = 0

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.counter +=1 # count this task
        self.user_to_task_map[userId].add(
            Task(task_id=self.counter, task_description=taskDescription, due_date=dueDate, tags=tags)
        )
        return self.counter
        
    def getAllTasks(self, userId: int) -> List[str]:
        # return list(map(lambda x: x.task_description, list(sorted(filter(lambda x: not x.is_complete, self.user_to_task_map[userId]), key=lambda y: y.due_date))))

        return list(map(lambda x: x.task_description, list(filter(lambda x: not x.is_complete, self.user_to_task_map[userId]))))

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        # return list(map(lambda x: x.task_description, list(sorted(filter(lambda x: not x.is_complete and tag in x.tags, self.user_to_task_map[userId]), key=lambda y: y.due_date))))
        return list(map(lambda x: x.task_description, list(filter(lambda x: not x.is_complete and tag in x.tags, self.user_to_task_map[userId]))))

    def completeTask(self, userId: int, taskId: int) -> None:
        designated_task = list(filter(lambda x: x.task_id == taskId, self.user_to_task_map[userId]))
        if not designated_task:
            return

        designated_task[0].is_complete = True
        

        


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)
