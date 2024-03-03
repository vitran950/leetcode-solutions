# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        count = 0
        while dummy:
            count += 1
            dummy = dummy.next

        if count == 1:
            return None

        if count == n:
            return head.next
        
        curr = head
        for _ in range(count - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head
