class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for index,val in enumerate(s):
            lastIndex[val] = index


        res = []
        size,end = 0,0
        for index,val in enumerate(s):
            size += 1
            end = max(lastIndex[val],end)
            if index == end:
                res.append(size)
                size = 0
        
        return res