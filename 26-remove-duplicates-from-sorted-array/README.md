# LeetCode: 26 - Remove duplicates from sorted array - Solution

## Intuition
The Problem states we are given a sorted array, and we need to remove dupicate values from the array `in-place`. We need to return the number of unique elements `k`.

## Approach
The approach is to iterate over the array, and compare and assign to the current position, the values not equal to the next position. IF the value is unequal we assign it to the current position held in variable `k`, and increase `k`. We return the value of `k + 1` as the result as `k` is the index value.

By iterating the whole array once, we avoid any extra space, and solve the problem with Time complexity of O(n).

## Time complexity: $$O(n)$$

## Space complexity: $$O(1)$$

#### Java
```java []
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
```

#### Python 3
```python []
class Solution:
	def removeDuplicates(self, nums: list[int]) -> int:
		k = 0
		for i in range( 1, len(nums) ):
			if nums[k] != nums[i]:
				k += 1
				nums[k] = nums[i]

		return k + 1
```
