class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        zero_cunt = 0 
        for num in nums:
            if num == 0:
                zero_cunt += 1 
            else:
                pro *= num

        ans = [0]*len(nums)

        if zero_cunt > 1:
            return ans
        
        elif zero_cunt == 1:
            ind = -1
            product = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    ind = i
                    continue 
                else:
                    product *= nums[i]
            ans[ind] = product 
            return ans 
        
        else:
            for i in range(len(nums)):
                ans[i] = pro//nums[i]
            return ans 