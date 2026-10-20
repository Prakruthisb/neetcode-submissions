class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1) 
        n2 = len(nums2)

        if n1>n2:
            nums1,nums2 = nums2,nums1
            n1,n2 = n2,n1

        left_half = (n1+n2+1)//2

        l,r = 0,n1
        while l<=r:
            m = (l+r)//2
            mid1 = m
            mid2 = left_half-m
            l1 = nums1[mid1-1] if mid1-1 >= 0 and mid1-1<n1 else float('-inf')
            l2 = nums2[mid2-1] if mid2-1 >= 0 and mid2-1<n2 else float('-inf')

            r1 = nums1[mid1] if mid1>=0 and mid1<n1 else float('inf')
            r2 = nums2[mid2] if mid2>=0 and mid2<n2 else float('inf') 

            if l1 > r2:
                r = m - 1 
            elif l2 > r1:
                l = m + 1 
            elif (n1+n2) % 2 == 0:
                return (max(l1,l2) + min(r1,r2)) / 2
            else:
                return max(l1,l2)