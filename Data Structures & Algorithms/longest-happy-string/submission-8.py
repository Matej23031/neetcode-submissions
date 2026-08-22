class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = [(-x,y) for x,y in ((a,"a"),(b,"b"),(c,"c")) if(x)]
        heapq.heapify(heap)
        stack = []
        res = ""
        while heap:
            count,letter = heapq.heappop(heap)
            if len(stack) > 1 and stack[-1] == stack[-2] == letter:
                if not heap:
                    break
                count2, letter2 = heapq.heappop(heap)
                res += letter2
                count2 += 1
                stack.append(letter2)
                if count2:
                    heapq.heappush(heap,(count2,letter2))

            else:
                res += letter 
                count += 1
                stack.append(letter)
            if count:
                heapq.heappush(heap,(count,letter))
        
        return res 