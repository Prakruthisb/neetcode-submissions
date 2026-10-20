class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        arr = []
        for i in range(n):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                arr.append(triplets[i])

        temp = []

        if not arr:
            return False

        temp.append(arr[0])
        n = len(arr)

        for i in range(1,n):
            t1 = temp.pop()
            t2 = arr[i] 
            t = []
            
            for i in range(3):
                if max(t1[i],t2[i]) > target[i]:
                    break 
                t.append(max(t1[i],t2[i]))
            if len(t) == 3:
                temp.append(t)
            else:
                temp.append(t2)
        
        return temp[0] == target