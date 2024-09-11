# LeetCode: 219. Contains Duplicate II - Python Solution

## Intuition
Given an integer array `nums` and an integer `k`, return true if there are two distinct indices `i` and `j` in the array such that `nums[i]` == `nums[j]` and `abs(i - j) <= k`.

We are given two things, one an int array `nums` and an int number `k`. And two conditions. We need to find 2 values in the given array that are equal, viz. `nums[i]` == `nums[j]` , and also that `abs( i - j )` <= `k`.

## Approach
I would like to approach the problem with a hashmap. I would store each value with its corresponding indice in the hasmap `hashmap_arr`. We then iteterate over nums. checking if the current value `nums[i]` is present in the hashmap, which would check the first condition `nums[i] == nums[j]`. And we check if current indice minus the indice of the found number in `hashmap_arr` is less than or equal to the given number `k`. viz `abs( i - hashmap_arr[nums[i]]) ) <= k`

## Complexity
- Time complexity: $$O(n)$$
  Since we are iterating over the array `nums` our time complexity is $$O(n)$$.

- Space complexity: $$O(n)$$
  Since we have a hashmap `hashmap_arr` which is the size of array `nums` we can say that then space complexity of the solution is $$O(n)$$.

#### Code - Python
```python3 []
class Solution:
	def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
		hashmap_arr = {}
		for i in range( 0, len( nums ) ):
			if nums[i] in hashmap_arr and abs( i - hashmap_arr[ nums[i] ] ) <= k:
				return True
			hashmap_arr[nums[i]] = i
		return False
```

# *Please UpVote, Gies me envouragement. :-)*