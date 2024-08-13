import java.util.Arrays;

class Solution {
    public int removeDuplicates(int[] nums) {
 		int k = 0;
		for ( int i = 0; i < nums.length; i++ ) {
			if ( nums[k] != nums[i] ) {
				k += 1;
				nums[k] = nums[i];
			}
		}
		return k + 1;
	}

	public static void main( String[] args ) {
		Solution solution = new Solution();

		int[] nums = {1,1,2};
		int[] expectedNums = {1,2,2};

		System.out.println(Arrays.toString( nums) );
		int k = solution.removeDuplicates(nums);
		System.out.println(Arrays.toString( nums) );
		System.out.println(k);

		if ( k == 2 ){
			System.out.println( "all good" );
		}

		for ( int i = 0; i < nums.length; i++ ) {
			if ( nums[i] != expectedNums[i] ) {
				System.out.println( "Not equal" + i + nums[i] + expectedNums[i] );
				break;
			}
		}
	}
}