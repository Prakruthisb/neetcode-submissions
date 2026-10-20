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

        while cur1 or cur2 or carry:
            s = 0 
            if cur1:
                s += cur1.val 
            if cur2:
                s += cur2.val 
            if carry:
                s += carry 

            val = s % 10 
            carry = s // 10 

            dummy.next = ListNode(val)

            cur1 = cur1.next if cur1 else cur1
            cur2 = cur2.next if cur2 else cur2
            dummy = dummy.next 
        
        return head.next