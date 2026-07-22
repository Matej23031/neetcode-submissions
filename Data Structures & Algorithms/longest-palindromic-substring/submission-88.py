class Solution:

    def longestPalindrome(self, nums: str) -> str:
        
        max_len = -math.inf
        res = []
        l,r = 0,0
        
        for i in range(len(nums)):
            l,r = i,i
            while l >= 0 and r < len(nums) and nums[r]  == nums[l]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    res = nums[l : r + 1] 
                l -= 1
                r += 1
            
            l,r = i,i + 1
            while l >= 0 and r < len(nums) and nums[r] == nums[l]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    res = nums[l : r + 1]
                l -= 1
                r += 1
        

        return res


        


            
        