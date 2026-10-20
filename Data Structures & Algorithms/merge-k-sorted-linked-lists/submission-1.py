# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            m = ListNode()
            dummy = m

            while l1 and l2:
                if l1.val <= l2.val:
                    m.next = l1 
                    l1 = l1.next 
                else:
                    m.next = l2 
                    l2 = l2.next 
                m = m.next 
            
            while l1:
                m.next = l1 
                l1 = l1.next 
                m = m.next 
            
            while l2:
                m.next = l2
                l2 = l2.next 
                m = m.next 
            
            return dummy.next

        def divide(lists):
            if len(lists) == 1:
                return lists[0]
            m = len(lists) // 2
            l = divide(lists[:m])
            r = divide(lists[m:])

            return merge(l,r)

        if not lists:
            return None
        
        return divide(lists)