class Solution {
    public int maxProfit(int[] prices) {
		if ( prices.length == 0 || prices.length == 1 ){
			return 0;
		}

		int min_price = prices[0];
		int max_profit = 0;
		int profit = 0;

		for ( int price: prices ) {
			if ( min_price > price ) {
				min_price = price;
			}

			profit = price - min_price;

			if ( profit > max_profit ) {
				max_profit = profit;
			}
		}
		return max_profit;
	}
	public static void main( String[] args ) {
		Solution sol = new Solution();
		//int[] prices = {7,1,5,3,6,4};
		int[] prices = {7,6,4,3,1};
		int profit = sol.maxProfit( prices );
		System.out.println( profit );
	}
}