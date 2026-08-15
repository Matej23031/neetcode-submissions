class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        cnt = 0
        def dfs(total,i):
            nonlocal cnt 
            if (total,i) in memo:
                return memo[(total,i)]
            if (i == len(coins) or total > amount):
                return 0
            if (total == amount):
                return 1

            skip = dfs(total, i + 1)
            use = dfs(total + coins[i],i)

            result = skip + use 
            memo[(total,i)] = result

            return result 

        return dfs(0,0)