# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            current_level = len(queue)
            for _ in range(current_level):
                node = queue.popleft()
                temp_left = node.left
                temp_right = node.right
                node.left = temp_right
                node.right = temp_left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root