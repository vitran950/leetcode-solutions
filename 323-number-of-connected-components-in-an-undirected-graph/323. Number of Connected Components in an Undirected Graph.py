from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for i in hash[node]:
                if i not in seen:
                    seen.add(i)
                    dfs(i)

        hash = defaultdict(list)
        for edge in edges:
            hash[edge[0]].append(edge[1])
            hash[edge[1]].append(edge[0])

        seen = set()
        ans = 0

        for element in range(n):
            if element not in hash:
                ans += 1
            else:
                item = hash[element]
                for curr in item:
                    if curr not in seen:
                        seen.add(curr)
                        ans += 1
                        dfs(curr)

        return ans