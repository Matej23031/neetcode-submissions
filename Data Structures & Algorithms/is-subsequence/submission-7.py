class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        q = deque(s)
        def dfs(i,remain,q):
            if not q:
                return True
            if i >= len(t):
                return False 
            

            if remain[i] == q[0]:
                q.popleft()
                return dfs(i + 1,remain,q)

            else:
                return dfs(i + 1,remain, q)
        
        return dfs(0,t,q)
        