class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        count = Counter(nums)

        res = []
        perm = []
        def dfs():
            nonlocal count
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    perm.append(c)
                    dfs()
                    perm.pop()
                    count[c] += 1
            
        dfs()
        return res