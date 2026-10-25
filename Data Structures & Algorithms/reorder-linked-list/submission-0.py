# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = 0
        temp = head
        revd = None

        while temp:
            temp2 = revd
            revd = ListNode()
            revd.val = temp.val
            revd.next = temp2
            temp = temp.next
            s += 1
        
        half = s // 2
        temp = head
        for i in range(half):
            temp2 = temp.next
            temp.next = ListNode()
            temp = temp.next
            temp.val = revd.val
            if i == half - 1 and s % 2 == 0:
                temp.next = None
            else:
                temp.next = temp2
            temp = temp.next
            revd = revd.next
        if temp:
            temp.next = None

