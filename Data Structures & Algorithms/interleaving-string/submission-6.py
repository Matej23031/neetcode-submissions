class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i,j,k):
            if k == len(s3):
                return True 
            if (i,j,k) in memo:
                return memo[(i,j,k)]

            result = False 

            if i < len(s1) and s1[i] == s3[k]:
                result = result or  dfs(i + 1,j,k + 1)
            
            if j < len(s2) and s2[j] == s3[k]:
                result = result or dfs(i,j + 1, k + 1)
            
            memo[(i,j,k)] = result
            return result
        
        return dfs(0,0,0)