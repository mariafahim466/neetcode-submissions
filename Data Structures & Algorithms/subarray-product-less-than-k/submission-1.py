class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        


        valid = 0 

        l = 0 

        product = 1 

        for r in range(len(nums)): 
            product *= nums[r] # 10 

            while l <= r and product >= k: 
                product = product // nums[l]
                l += 1 

            # # check again AFTER updating l 
            # if product < k: 
            valid += r-l+1



        return valid 

         