# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(first, second):
            if (not first and second) or (first and not second):
                return False

            if not first and not second:
                return True

            # if (not first.left and second.left) or (first.left and not second.left):
            #     return False
            # if (not first.right and second.right) or (first.right and not second.right):
            #     return False

            if first.val != second.val:
                return False
            return dfs(first.left, second.left) and dfs(first.right, second.right)

        return dfs(p, q)