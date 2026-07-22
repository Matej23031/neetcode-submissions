class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def perm(i,nums):
            if i == len(nums):
                return [[]]

            temp = []
            perms = perm(i + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    temp.append(p[:j] + [nums[i]] + p[j:])

            return temp

        perm(0,nums)

        return perm(0,nums)
        


