# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2 

        head = ListNode()
        dummy = head 
        carry = 0 
        c = False 

        while cur1 and cur2:
            s = cur1.val + cur2.val + carry 
            if s >= 10:
                c = True 
            else:
                c = False 
            val = s % 10 
            carry = s // 10 

            dummy.next = ListNode(val)

            cur1 = cur1.next 
            cur2 = cur2.next
            dummy = dummy.next 
        
        while cur1:
            s = cur1.val + carry 
            if s >= 10:
                c = True 
            else:
                c = False 
            val = s % 10 
            carry = s // 10 

            dummy.next = ListNode(val)

            cur1 = cur1.next
            dummy = dummy.next 
        
        while cur2:
            s = cur2.val + carry 
            if s >= 10:
                c = True 
            else:
                c = False 
            val = s % 10 
            carry = s // 10 

            dummy.next = ListNode(val)

            cur2 = cur2.next
            dummy = dummy.next

        if c:
            dummy.next = ListNode(carry)
        
        return head.next