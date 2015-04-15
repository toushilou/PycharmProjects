#! /usr/bin/env python
#coding=utf-8
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        hasBought = False
        index = 0
        buyPrice = 0
        sellPrice = 0
        profit = 0
        size = len(prices)
        if size != 1:
            for index in range(size):
                if index == size - 1:
                    if hasBought == True:
                        profit += prices[index] - buyPrice
                    return profit
                if prices[index] <= prices[index + 1]:
                    if hasBought == False:
                        hasBought = True
                        buyPrice = prices[index]
                else:
                    if hasBought == True:
                        sellPrice = prices[index]
                        profit += sellPrice - buyPrice
                        hasBought = False
        return profit

s = Solution()
print s.maxProfit([2,1])