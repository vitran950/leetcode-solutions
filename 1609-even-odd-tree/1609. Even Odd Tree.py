# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0 
        while queue:
            current_level = len(queue)
            arr_to_check = []
            for _ in range(current_level):
                node = queue.popleft()
                arr_to_check.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            prev = arr_to_check[0]
            if len(arr_to_check) > 1:
                for i in range(1, len(arr_to_check)):
                    if level % 2 == 0: # even indexed level
                        if arr_to_check[i] % 2 == 0 or arr_to_check[i] <= prev:
                            return False
                    else: # odd indexed level
                        if arr_to_check[i] % 2 != 0 or arr_to_check[i] >= prev:
                            return False
                    prev = arr_to_check[i]
            else: 
                if (level % 2 == 0 and prev % 2 == 0) or (not level % 2 == 0 and not prev % 2 == 0):
                    return False
            level += 1
        return True