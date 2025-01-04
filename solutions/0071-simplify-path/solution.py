from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:

        q = deque()
        pathlist = path.split("/")

        n = len(pathlist)
        if n <= 1:
            return path
        
        i = 0
        while i < n:
            next_token = pathlist[i]
            if next_token == "..":
                if len(q) > 0:
                    popped = q.pop()
            elif next_token == "" or next_token == ".":
                i += 1
                continue
            else:
                q.append(next_token)
            i += 1

        # print("queue = ", q)
        dq = "/".join(q)
        return "/" + dq


                
        
