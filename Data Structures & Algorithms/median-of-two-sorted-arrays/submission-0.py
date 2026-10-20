class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        l,r = 0,0
        n1 = len(nums1)
        n2 = len(nums2)

        while l<n1 and r<n2:
            if nums1[l] < nums2[r]:
                arr.append(nums1[l])
                l += 1 
            else:
                arr.append(nums2[r])
                r += 1 
        
        while l<n1:
            arr.append(nums1[l])
            l += 1
        while r<n2:
            arr.append(nums2[r])
            r += 1 
        
        n = len(arr)
        mid = n//2
        if n%2 == 0:
            return (arr[mid] + arr[mid-1])/2
        else:
            return arr[mid]