class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # what do we want: 
        # we want the length of the longest consecutive sequence of elements that can be formed 
        nums.sort() 
        nums_set = set(nums)
        count = 1 
        maxi = 0
        if len(nums) == 1: 
            return 1 
        for num in nums_set: 
            if num - 1 not in nums_set:
                count = 1  
                while num + count in nums_set: 
                    count += 1 
            maxi = max(count, maxi)
        return maxi 


