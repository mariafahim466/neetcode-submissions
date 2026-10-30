class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # start both at index 1 cuz we always wanna keep the first one
        k = 1

        for r in range(1, len(nums)): 
            if nums[r] != nums[r-1]: 
                nums[k] = nums[r]
                k += 1 

        return k 
        