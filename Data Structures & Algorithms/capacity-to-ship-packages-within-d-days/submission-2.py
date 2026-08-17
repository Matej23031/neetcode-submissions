class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)
        res = right
        def canShip(cap):
            cntShip = 1 
            curCap = cap
            for w in weights:
                if curCap - w < 0:
                    cntShip += 1
                    curCap = cap
                curCap -= w
            
            return cntShip <= days
                
        
        while left <= right:
            cap = (left + right) // 2

            if canShip(cap):
                res = min(res,cap)
                right = cap - 1
            else:
                left = cap + 1

        return res