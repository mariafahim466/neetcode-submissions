class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = [] 

        left = 0
        right = len(nums) - 1 


        my_dict = {}
        # while they're both not at the end
        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in my_dict: 
                final.append(my_dict[diff])
                final.append(i)
                return final
            else: 
                my_dict[nums[i]] = i 


