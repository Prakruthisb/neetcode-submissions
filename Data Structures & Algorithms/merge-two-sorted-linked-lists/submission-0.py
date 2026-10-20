# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = ListNode()
        cur = arr
        
        while list1 and list2:
            if list1.val < list2.val:
                arr.next = ListNode(list1.val)
                arr = arr.next
                list1 = list1.next 
            else:
                arr.next = ListNode(list2.val)
                arr = arr.next
                list2 = list2.next 
        
        while list1:
            arr.next = ListNode(list1.val)
            arr = arr.next
            list1 = list1.next 
        while list2:
            arr.next = ListNode(list2.val)
            arr = arr.next
            list2 = list2.next

        return cur.next 