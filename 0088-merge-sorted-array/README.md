# LeetCode 88 - Merge sorted array - Solution

## Intuition
We are given two sorted arrays nums1 and nums2, in non decreasing orders, and 2 numbers m and n. Where m and n are elements we need to merge from the two arrays. The length of nums1 = m+n and length of nums2 is n. We need to merge the two already sorted arrays and the result should be stored in nums1.

## Approach
We can use 2 pointers, and start merging from the i'th and j'th position of the arrays, where i = m - 1 and j = n - 1, and we use another pointer k where k = m + n - 1 to store where the larger element will be placed. We compare the elements in nums1 and nums2 and place the larger element in nums1 at the kth element. We keep doing this till j >= 0. For the remaining elements in nums1, we don't do anything as they are already sorted.

## Time complexity: $$O(m+n)$$
`We iterate through both the arrays once so time complexity is $$O(m+n)$$`

## Space complexity: $$O(1)$$
`We are not using any extra space so space complexity is $$O(1)$$`

### Python Notes:
Because everything in Python is an object, when doing nums1 = sorted(nums1[:m] + nums2[:n]) two things happen:

a new object is created which is the result of sorted(nums1[:m] + nums2[:n]), while the original nums1 that was passed in to the function remains untouched
So the line nums1 = sorted(nums1[:m] + nums2[:n]) is actually equivalent to nums1 = new object, i.e. the address of new object is now assigned to nums1

But since the problem requires modifying the original object nums1, you get an error.
However, when using nums1[:], you fill up the indices of the original nums1 with new values, so the original nums1 is indeed sorted by the end.

#### Python3
```python []
class Solution:
	def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		# nums1[:] = nums1[:(m+n)] + [0] * ( (m+n) - len( nums1 ) )
		i = m - 1
		j = n - 1
		k = m + n - 1

		while j >= 0:
			if ( i >= 0 and nums1[i] > nums2[j] ):
				nums1[k] = nums1[i]
				i -= 1
			else:
				print( 'inside: ', k, i, j, nums1[i], nums2[j] )
				nums1[k] = nums2[j]
				j -= 1
			k -= 1

		return nums1
```

#### Java
```java []
import java.util.*;

class Solution {
	 /**
	 * @param nums1
	 * @param m
	 * @param nums2
	 * @param n
	 */
	public void merge(int[] nums1, int m, int[] nums2, int n) {
		if ( n <= 0 ) {
			return;
		}
		int i = m - 1;
		int j = n - 1;
		int k = m + n - 1;
		while( j >= 0 ) {
			if( i >= 0 && nums1[i] > nums2[j] ) {
				nums1[k] = nums1[i];
				i--;
			} else {
				nums1[k] = nums2[j];
				j--;
			}
			k--;
		}
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] s1_nums1 = {1,2,3,0,0,0,0};
		int s1_m = 3;
		int[] s1_nums2 = {2,5,6,7};
		int s1_n = 4;
		sol.merge( s1_nums1, s1_m, s1_nums2, s1_n );
		System.out.println( "out: " + Arrays.toString( s1_nums1 ) );

		int[] s2_nums1 = {1,2,3,0, 0};
		int s2_m = 3;
		int[] s2_nums2 = {2,5,6};
		int s2_n = 2;
		sol.merge( s2_nums1, s2_m, s2_nums2, s2_n );
		System.out.println( "out: " + Arrays.toString( s2_nums1 ) );

		int[] s3_nums1 = {1};
		int s3_m = 1;
		int[] s3_nums2 = {};
		int s3_n = 0;
		sol.merge( s3_nums1, s3_m, s3_nums2, s3_n );
		System.out.println( "out: " + Arrays.toString( s3_nums1 ) );

		int[] s4_nums1 = {0};
		int s4_m = 0;
		int[] s4_nums2 = {1};
		int s4_n = 1;
		sol.merge( s4_nums1, s4_m, s4_nums2, s4_n );
		System.out.println( "out: "+Arrays.toString( s4_nums1 ) );
	}
}
```
