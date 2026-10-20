# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        cur = head 
        while cur:
            length += 1 
            cur = cur.next
        
        ind = length - n
        i = 0 
        temp,cur = head,head

        if ind == 0:
            return cur.next 
        
        while cur:
            if i==(ind-1):
                cur.next = cur.next.next
            cur = cur.next 
            i += 1 
        
        return temp 