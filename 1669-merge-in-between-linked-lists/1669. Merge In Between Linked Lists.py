# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        slow = list1
        fast = list1.next
        count = 1
        while count < a:
            slow = slow.next
            fast = fast.next
            count += 1

        fast2 = fast
        while count <= b:
            fast2 = fast2.next
            count += 1

        last = ListNode()
        last.next = fast2
        
        while list2:
            slow.next = list2
            list2 = list2.next
            slow = slow.next
        
        slow.next = last.next
        return list1
