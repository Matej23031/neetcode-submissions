class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for rox in range(1,n):
            dp[0][rox] = dp[0][rox - 1] + grid[0][rox]

        for roy in range(1,m):
            dp[roy][0] = dp[roy-1][0] + grid[roy][0]         



        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j],dp[i][j - 1])
                
        return dp[-1][-1]

