from collections import deque, defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = defaultdict(list)
        for i in range(m):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque([src])
        while q:
            node = q.popleft()

            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
        dist = [-1 if d == float('inf') else d for d in dist]

        return dist
