# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:24
# @Author  : banshaohuan
# @Site    : 
# @File    : Best Time to Buy and Sell Stock II.py
# @Software: PyCharm
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i = 0
        j = 1
        length_prices = len(prices)

        while j < length_prices:
            if prices[i] < prices[j]:
                profit += prices[j] - prices[i]

            i += 1
            j += 1

        return profit
