class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        mapa = {}

        for i,n in enumerate(nums):
            mapa[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapa and i != mapa[diff]:
                return [i,mapa[diff]]
        
        return []