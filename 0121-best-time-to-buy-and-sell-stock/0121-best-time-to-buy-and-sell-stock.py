class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        maximum=0
        minimum=prices[0]
        profit = 0
        for i in prices:
            minimum = min(minimum,i)
            profit=i-minimum
            maximum=max(profit,maximum)
        return maximum
        