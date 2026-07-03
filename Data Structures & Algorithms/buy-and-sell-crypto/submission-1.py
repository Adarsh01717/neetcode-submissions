class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        res = 0
        buy = prices[0]  
        
        for i in prices:
            if i < buy:
                buy = i  
            else:
                res = max(res, i - buy)  
                
        return res