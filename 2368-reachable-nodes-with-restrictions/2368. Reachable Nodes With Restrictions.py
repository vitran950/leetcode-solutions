from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    count += 1
                    dfs(neighbor)
        
        graph = defaultdict(list)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        seen = set(restricted)
        if 0 not in seen:
            count += 1
            seen.add(0)
            dfs(0)
        
        return count