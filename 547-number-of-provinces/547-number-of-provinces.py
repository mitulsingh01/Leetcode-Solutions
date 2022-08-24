class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        v = len(isConnected)
        adj = [[] for _ in range(v)]
        for i in range(v):
            for j in range(v):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
                    adj[j].append(i)
        vis = [[] for _ in range(v)]
        count = 0
        for i in range(v):
            if not vis[i]:
                count += 1
                self.dfs(i, adj, vis)
        return count
    def dfs(self, node, adj, vis):
        vis[node] = 1
        for i in adj[node]:
            if not vis[i]: self.dfs(i, adj, vis)
                    