# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        if not head:
            return None
        while head:
            temp = ListNode()
            temp.val = head.val
            head = head.next
            temp.next = res
            res = temp
        
        return res