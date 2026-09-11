class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l,r = 0,1
        maxprof = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprof = max(profit, maxprof)
            else:
                l = r
            r +=1
        return maxprof

        
        