import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * # Intuition
 * The problem states we have Int array `nums` with `n` elements, and we need to find the majority element. Any element which appears more than `n/2` times is the majority element.
 * 
 * # Approach
 * From the problem itself we can deduce that the best approach is to use a HashMap, to count the number of times each element `n` appears in the array `nums`. As soon as we find any element which has appeard more than `n/2` times we return it as the answer.
 * 
 * # Complexity
 * - Time complexity: O(n)
 * 
 * - Space complexity: O(1)
 */
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap<>();

		for ( int i = 0; i < nums.length; i++ ) {
            hashmap.put(nums[i], hashmap.getOrDefault(nums[i], 0) + 1);
			if ( hashmap.get(nums[i]) > nums.length/ 2 ) {
				return nums[i];
			}
		}
		return -1;
    }

	public static void main( String[] args ) {
		Solution sol = new Solution();
		int[] arr = {2,2,1,1,1,2,2};
		int cnt = sol.majorityElement( arr );
		System.out.println(cnt);
	}
}
