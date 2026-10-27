class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
           
        n = len(nums)
        ans = [] # hold our final result 
        sol = [] # intermediate steps 

        def backtrack(): 
            # we're at a base case if len = n 
            if len(sol) == n: 
                ans.append(sol[:])
                return 
            # if we're not at a base case, we wanna loop over the numbers 
            for x in nums: 
                if x not in sol: 
                    sol.append(x)
                    backtrack()
                    # when we're done we remove it so we can go back and do it for the other nums 
                    sol.pop() 


        backtrack() 
        return ans 