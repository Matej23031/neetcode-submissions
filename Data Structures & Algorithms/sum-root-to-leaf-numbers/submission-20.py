from functools import cache 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        suma = 0

        def dfs(string,root):
            nonlocal suma
            string = string + str(root.val)
            if root.left is None and root.right is None:
                suma = suma + int(string)
                return 0

            if root.left:
                dfs(string,root.left)
            if root.right:
                dfs(string,root.right)
            return 1  
        
        dfs("",root)
        return suma
