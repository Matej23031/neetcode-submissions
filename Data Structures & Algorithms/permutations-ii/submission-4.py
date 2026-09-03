class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        count = Counter(nums)
        temp = []
        res = []
        def dfs():
            if len(temp) == len(nums):
                res.append(temp.copy())
                return

            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    temp.append(c)
                    dfs()
                    count[c] += 1
                    temp.pop()
            
        dfs()
        return res