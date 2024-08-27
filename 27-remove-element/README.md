# LeetCode: 27 - Remove element - Solution

## Intuition
The problem gives us an array of elements `nums`, and a value `val`, we need to remove all values of the array equal to `val` in place. The resultant array is where the first `count` elements are not equal to `val` and we need to return `count`, the number of values in the array not equal to `val`.

## Approach
The approach is to iterate over the array and assign values not equal to `val` to the current location, held by `count`, and incrememnt `count`. This helps create a subarray in front of the array, keeping track of the number of elements in the variable `count`. The remaining elements can be ignored and are irrelevant.

By iterating the whole array once, you avoid any extra space, and solve the problem with O(n) complexity.

## Time complexity: $$O(n)$$

## Space complexity: $$O(1)$$

#### Java
```java []
class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        for(int i = 0; i < nums.length; i++ ) {
            if ( nums[i] != val ){
                nums[count] = nums[i];
                count++;
            }
        }
        return count;
    }
}
```

#### Python3
```python []
class Solution:
	def removeElement(self, nums: list[int], val: int) -> int:
		count = 0
		for i in nums:
			if i != val:
				nums[count] = i
				count += 1

		return count
```
