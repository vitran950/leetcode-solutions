# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parents):
            if not node:
                return 0

            temp = 0
            for parent in parents:
                temp = max(temp, abs(parent - node.val))

            # Make new lists so left and right don't share state
            new_parents = parents + [node.val]

            left = dfs(node.left, new_parents)
            right = dfs(node.right, new_parents)

            return max(temp, left, right)

        return dfs(root, [])