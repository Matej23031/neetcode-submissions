class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        

        curSum = 0
        maxSum = 0
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(curSum,0)
            curSum += nums[i]
            maxSum = max(curSum,maxSum)
        
        if maxSum == 0:
            return max(nums) 

        return maxSum
            
            
            