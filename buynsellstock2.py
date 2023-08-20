"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions."""
def maxProfit(prices):
    buy1 = float('-inf')
    sell1 = 0
    buy2 = float('-inf')
    sell2 = 0

    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2
