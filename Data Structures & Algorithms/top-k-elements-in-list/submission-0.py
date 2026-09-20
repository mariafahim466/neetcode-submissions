class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        my_dict = {} 
        output = [] 

        for num in nums: 
            if num in my_dict: 
                my_dict[num] += 1
            else: 
                my_dict[num] = 1 
        
        my_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
        
        for key in list(my_dict.keys())[:k]:
            output.append(key)

        return output
