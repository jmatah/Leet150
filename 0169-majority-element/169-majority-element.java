import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
