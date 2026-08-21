class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        mapa = defaultdict(int)

        for num in nums:
            mapa[num] = 1 + mapa.get(num,0)
        
        n = len(nums) / 3 

        res = []
        for num,cnt in mapa.items():
            if cnt > n:
                res.append(num)
        
        return res