from collections import defaultdict
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(node):
            for element in graph[node]:
                if element not in seen:
                    seen.add(element)
                    if arr[element] == 0:
                        return True
                    if dfs(element):
                        return True
            return False

        graph = defaultdict(list)
        for i, num in enumerate(arr):
            num1 = i + num
            num2 = i - num
            if 0 <= num1 < len(arr):
                graph[i].append(num1)
            if 0 <= num2 < len(arr):
                graph[i].append(num2)
        
        seen = set()
        return dfs(start)