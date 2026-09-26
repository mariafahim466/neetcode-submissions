class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    

        # given an int array nums
        # return all the triplets 
        final = [] 
        l = 0 
        r = len(nums) - 1
        nums.sort() 
# [-1,0,1,2,-1,-4]
        used = set() 
        for i in range(len(nums)): 
            if nums[i] in used: 
                continue
            
            l = i + 1 
            r = len(nums) - 1 
            while l < r: 
                if nums[l] + nums[r] == -(nums[i]): 
                    used.add(nums[i])
                    final.append([nums[l], nums[r], nums[i]])
                    l += 1 
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1 
                elif nums[l] + nums[r] < -(nums[i]): 
                    # our values too small, inc the left 
                    l += 1 
                elif nums[l] + nums[r] > -(nums[i]): 
                    r -= 1 
        
        return final 















        # left = 0 
        # right = len(nums) - 1
        # nums.sort() 
        # big_list = [] 

        # for i in range(len(nums)): 
        #     if nums[left] + nums[right] > nums[i]: 
        #         right -= 1 
        #     elif nums[left] + nums[right] < nums[i]: 
        #         left += 1 
        #     else: 
        #         mini_list = [left, right, i]
        #         big_list.append(mini_list)

        # return big_list 



