class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(node, left, right):
            if len(node) == n*2:
                ans.append(node)
                return
            if left == n and right < left:
                dfs(node + ')', left, right + 1)
                return
            elif right == left:
                dfs(node + '(', left + 1, right)
                return
            else:
                dfs(node + '(', left + 1, right)
                dfs(node + ')', left, right + 1)
                return
            return
        ans = []
        curr = '('
        dfs(curr, 1, 0)
        return ans
