from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        ves = 0
        max_cnt = 0
        
        max_lis = 1
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],LIS[j] + 1)
                    max_lis = max(LIS[i],max_lis)                
        
        return max_lis