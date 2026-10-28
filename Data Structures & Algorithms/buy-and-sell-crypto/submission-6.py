class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       l, r = 0, 1
       n = len(prices)
       max_profit = 0 
       max_l = 0 


       for r in range(n): 
    

        max_profit = max(max_profit, prices[r]-prices[l])

        if prices[l] > prices[r]: 
            l = r
    
       return max_profit
       
       