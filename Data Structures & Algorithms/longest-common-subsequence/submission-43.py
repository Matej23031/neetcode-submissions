class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cnt = 0
        cache = [[-float("inf")] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) + 1):
            cache[i][len(text2)] = 0
        for j in range(len(text2) + 1):
            cache[len(text1)][j] = 0
        
        for i in range(len(text1) - 1, - 1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    cache[i][j] = 1 + cache[i + 1][j + 1]
                else:
                    cache[i][j] = max(cache[i  +1][j],cache[i][j + 1])

        return cache[0][0]
