class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        selling = []
        buying = []
        i = 0
        while i < n-1:
            if prices[i] < prices[i+1]:
                buying.append(prices[i])
                selling.append(prices[i+1])
            i+=1    
        return sum([a - b for a,b in zip(selling,buying)])   
        