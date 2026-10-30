class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count_val = 0 
        n = len(nums)

        for i in range(n): 
            if nums[i] == val: 
                nums[i] = -1 
                count_val += 1 
        
        nums.sort() 
        nums.reverse() 
        print(nums)
        return n - count_val
