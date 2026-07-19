class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        count = 0
        seen = set()
        def dfs(node):
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        for i in range(len(adj)):
            if i not in seen:
                count += 1
                dfs(i)

        return count