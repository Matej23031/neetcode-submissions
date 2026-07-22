class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l,total = 0,0
        res = math.inf
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                res = min(res,r - l + 1)
                l += 1

        return 0 if res == float('inf') else res
                
                
        
        