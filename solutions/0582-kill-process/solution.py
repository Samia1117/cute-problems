class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        if kill == 0:
            return pid
        
        adj_dic = {}
        for proc_indx, parent in enumerate(ppid):
            if parent not in adj_dic:
                adj_dic[parent] = []
            adj_dic[parent].append(pid[proc_indx])
        
        # print(f"Adj dic: {adj_dic}")
        
        q = deque()
        q.append(kill)
        to_kill = set()

        while q:
            curr = q.popleft()
            to_kill.add(curr)
            if curr not in adj_dic:
                continue
            for neighbor in adj_dic[curr]:
                q.append(neighbor)
        return list(to_kill)

        
