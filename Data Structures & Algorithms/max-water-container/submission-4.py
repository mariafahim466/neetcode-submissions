class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # for each thing, 
        # i tihkn we shuold start l = 0 

        '''
        left = 0, right = end

        while left < right:
            calculate area, update max
            if height[left] < height[right]:
                left += 1      # short side is left, move it
            else:
                right -= 1     # short side is right, move it
        '''

        end = len(heights)
        left = 0 
        right = end -1
        # to get the area, do (right - left) - min(heights[left], heights[right])
        max_area = 0 
        while left < right: 
            current_area = (right-left) * min(heights[left], heights[right])
            max_area = max(max_area, current_area)

            if heights[left] < heights[right]: 
                left += 1
            else: 
                right -= 1 

        return max_area


