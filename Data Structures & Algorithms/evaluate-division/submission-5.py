class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        mapa = defaultdict(list)

        for i in range(len(values)):
            mapa[equations[i][0]].append((equations[i][1],values[i]))
            mapa[equations[i][1]].append((equations[i][0],1/values[i]))
        
        def bfs(src,target):
            if src not in mapa or target not in mapa:
                return -1.00
            visited = set()
            dq = deque([(src,1)])

            while dq:
                node,weight = dq.popleft()
                visited.add(node)
                if node == target:
                    return weight
                for nei,distance in mapa[node]:
                    if nei not in visited:
                        dq.append((nei,weight * distance))

            return -1.00
        
        ans = []
        for qu in queries:
            ans.append(bfs(qu[0],qu[1]))
        
        return ans