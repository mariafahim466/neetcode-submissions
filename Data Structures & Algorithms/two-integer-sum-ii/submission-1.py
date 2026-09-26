class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given an array of ints, numbers that's sorted in increasing order 
        left = 0 
        right = len(numbers) - 1

        while left < right: 
            summed = numbers[left] + numbers[right]
            if summed == target: 
                return [left+1, right+1]
            elif summed < target: # left needs to get bigger 
                left += 1 
            elif summed > target: 
                right -= 1
        

