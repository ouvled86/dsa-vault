# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False

        def addTwoNodes(l1, l2, prev=None):
            nonlocal carry
            if not l1 and not l2:
                if carry:
                    prev.next = ListNode(1)
                return

            if not l1 and l2:
                prev.next = l2
                l1 = l2
                l2 = None
            new_val = l1.val + (l2.val if l2 else 0)
            
            if carry:
                new_val += 1
                carry = False
            if l1:
                l1.val = new_val % 10
            if new_val > 9:
                carry = True
            
            addTwoNodes(l1.next, (l2.next if l2 else None), l1)

            
        
        addTwoNodes(l1, l2)
        return l1