class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

        if len(nums) == 1: 
            return nums

        final = [] 

        # create a dict 
        # for each one we add it to the dict with a count 
        # loop thru and return the first k values 

        track = {} 
        for x in nums: 
            if x in track: 
                track[x] += 1 
            else: 
                track[x] = 1 


        pairs = sorted(track.items(), key=lambda pair: pair[1], reverse=True)
        
        for n, v in pairs: 
            final.append(n)
        
 
        return final[:k]

    

