class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        profit = 0
        buyAt = [prices[0], 0]
        sellAt = [prices[0], 0]
        prices[0] = 0
        maxProfit = 0
        for i in range(1, len(prices)): 
            cur = prices[i]
            print(buyAt, sellAt, cur, prices)
            if (cur < sellAt[0] and  i - sellAt[1] > 1) or cur < buyAt[0]:
                buyAt[0] = cur
                buyAt[1] = i
                sellAt[0] = cur
                sellAt[1] = i
                prices[i] = prices[i-1]
                
            elif cur > sellAt[0]:
                sellAt[0] = cur
                sellAt[1] = i
                profit = (sellAt[0] - buyAt[0]) + prices[buyAt[1]]
                if maxProfit < profit:
                    maxProfit = profit
                prices[i] = profit
            else:
                prices[i] = prices[i-1]
        return max(maxProfit, profit)
s = Solution()
print('Profit:', s.maxProfit([2,1,4]))