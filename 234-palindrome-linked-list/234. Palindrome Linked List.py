# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i, j = 0, len(arr)-1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
        
        
#         def reverse(node):
#             prev = None
#             curr = node
#             while curr:
#                 next_temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = next_temp
#             return prev
        
#         slow, fast, count = head, head, 0
#         while fast and fast.next:
#             count += 1
#             slow = slow.next
#             fast = fast.next.next
        
#         # check if it's in the middle
#         if count % 2 == 1:
#             slow = slow.next
            
#         reverse_slow = reverse(slow)
        
#         while reverse_slow:
#             if head.val != reverse_slow.val:
#                 return False
#             head = head.next
#             reverse_slow = reverse_slow.next

#         return True