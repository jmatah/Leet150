"""
# Intuition
You are given an array prices where `prices[i]` is the price of a given stock on the `ith` day. Objective is to find the day you should buy and another day when you should sell, to attain max profit. The approach I have taken is to have a single pass over the array, keeping two variables `min_price`, `max_profit`, and Todays Profit as `profit`.

# Approach
Initially assigning todays profit as `prices[0]`, the current days price. We then iterate through the array once. IF we find that any days `price` is less than the min profit, we assign that price to the `min_price`. We calculate daily `profit`, and compare this to the `max_profit` we can have when we sell the stock. In the end we get the `max_profit` over the entire length of the period.

If the length of the array is `0` or `1`, we return `0` `max_profit`.

# Complexity
- Time complexity: O(n)
Since we are going through the entire array over only once.

- Space complexity: O(1)
Since we are only keep track of variables `min_price`, `max_profit` and `profit`.
"""
class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		if ( len( prices ) == 0 or len( prices ) == 1 ):
			return 0

		min_price = prices[0]
		max_profit = 0
		profit = 0

		for price in prices:
			if min_price > price:
				min_price = price

			profit = price - min_price

			if profit > max_profit:
				max_profit = profit

		return max_profit

sol = Solution()

prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
profit = sol.maxProfit( prices )
print( profit )