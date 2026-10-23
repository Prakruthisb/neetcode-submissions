# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head 
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        
        if n == 1:
            rev = prev.next 
        else:
            rev = prev
            i = 1
            while prev and prev.next:
                if i == n-1:
                    prev.next = prev.next.next 
                    break 
                i += 1 
                prev = prev.next
        
        cur = rev
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        return prev
        