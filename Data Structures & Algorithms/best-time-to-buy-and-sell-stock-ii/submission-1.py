class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: just add the profit each time we have an increase 
        l = 0 
        r = 1 
        profit = 0 

        for r in range(len(prices)): 
            curr = prices[r] - prices[l]

            if curr > 0: 
                profit += curr 
                l += 1 

            if prices[l] >= prices[r]: 
                l = r 
            
            
        return profit 