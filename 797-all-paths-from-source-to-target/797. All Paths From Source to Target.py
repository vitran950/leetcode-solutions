class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(curr):
            if curr[-1] == len(graph) - 1:
                ans.append(curr[:])
                return
            
            nums = graph[curr[-1]]
            for num in nums:
                curr.append(num)
                backtrack(curr)
                curr.pop()
        
        ans = []
        backtrack([0])
        return ans