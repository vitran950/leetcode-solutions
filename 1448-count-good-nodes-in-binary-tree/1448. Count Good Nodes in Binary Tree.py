# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, highest):
            if not node:
                return 0
            count = 1 if node.val >= highest else 0
            left = dfs(node.left, max(highest, node.val)) 
            right = dfs(node.right, max(highest, node.val))
            total = count + left + right
            return total

        return dfs(root, float('-inf'))

            