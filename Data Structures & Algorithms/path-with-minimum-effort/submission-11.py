class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS,COLS = len(heights), len(heights[0])
        minHeap = [[0,0,0]]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        effort = [[float("inf")] * COLS for _ in range(ROWS)]

        while minHeap: 
            eff, x , y = heapq.heappop(minHeap)
            
            if eff > effort[x][y]:
                continue 
            if x == ROWS -1 and y == COLS - 1:
                return eff
            
            for dx, dy in directions:
                nx,ny = dx + x, dy + y
                if not (0 <= nx < ROWS and 0 <= ny < COLS):
                    continue  
                newEffort = max(eff,abs(heights[x][y] - heights[nx][ny]))
                if newEffort < effort[nx][ny]:
                    effort[nx][ny] = newEffort 
                    heapq.heappush(minHeap,[newEffort,nx,ny])
        return effort[ROWS - 1][COLS - 1]