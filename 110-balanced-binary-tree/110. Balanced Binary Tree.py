# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True]
            
            left = dfs(node.left)
            right = dfs(node.right)

            curr = left[1] and right[1]
            if abs(left[0] - right[0]) > 1:
                curr = False
            
            final_depth = max(left[0], right[0]) + 1    
            return [final_depth, curr]
        
        ans = dfs(root)
        return ans[1]