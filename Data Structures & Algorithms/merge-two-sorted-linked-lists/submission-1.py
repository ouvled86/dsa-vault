# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        res = ListNode()
        temp = res
       
        while list1 and list2:
            if list1.val > list2.val:
                temp.val = list2.val
                temp.next = ListNode()
                temp = temp.next
                list2 = list2.next
            else:
                temp.val = list1.val
                temp.next = ListNode()
                temp = temp.next
                list1 = list1.next

        while list1:
            temp.val = list1.val
            if list1.next:
                temp.next = ListNode()
            temp = temp.next
            list1 = list1.next

        while list2:
            temp.val = list2.val
            if list2.next:
                temp.next = ListNode()
            temp = temp.next
            list2 = list2.next
        temp = None

        return res
    
