# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head 

        while cur.next and cur.next.next != cur:
            temp,p = cur.next,cur.next

            while p.next:
                if p.next.next == cur:
                    break 
                p = p.next 

            cur.next = p
            cur = temp
            p.next = cur 
        
        cur.next = None