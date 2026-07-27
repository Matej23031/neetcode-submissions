class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        openClose = {'}':'{',')':'(',']':'['}
        
        for ch in s:
            if ch in openClose:
                if stack and stack[-1] == openClose[ch]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(ch)
        

        return True if not stack else False
            