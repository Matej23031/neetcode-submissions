class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        end = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= end:
                end = i
                continue
            
        
        return True if end == 0 else False