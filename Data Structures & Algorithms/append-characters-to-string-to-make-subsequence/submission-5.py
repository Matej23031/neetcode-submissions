class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        
        ls,lt = 0,0
        while ls < len(s) and lt < len(t):
            if s[ls] == t[lt]:
                ls += 1
                lt += 1
            else:
                ls += 1
        
        return len(t) - lt