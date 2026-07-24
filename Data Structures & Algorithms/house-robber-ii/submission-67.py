class Solution:
    def helps(self,start,end,nums):
        length = end - start + 1
        dp = [0] * (length + 2)

        for i in range(end - 1 , start - 1,-1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        return max(dp[0],dp[1])



    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        window = len(nums) - 1

        start = 0 
        maks = 0
        end = window
        while end <= len(nums):
            maks = max(maks,self.helps(start,end,nums))
            start += 1
            end += 1
        
        return maks 

        
