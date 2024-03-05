# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = root.val
        while queue:
            length = len(queue)
            iteration = 0
            for _ in range(length):
                node = queue.popleft()
                if iteration == 0:
                    result = node.val
                iteration += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result