# LeetCode - 228. Summary Ranges - Python Solution

## Intuition
We are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

I would approach this problem via a 2 pointer approach.

## Approach
I would approach this problem with a single loop with 2 pointers with start `start_i` variable and a `end_i` variable. And a `hashmap_arr` list() for the result. 

We check whether the number at current indice and the number at the indice `end_i` have a differene of `1`. If yes we assign `end_i` to `i` and continue with the loop.

If the difference of number at the current indice and number at indice at `end_i` is geater than `1`, then we check if both pointers are the same number, we append number at the indice `end_i`, else we add `start_i -> end_i`.

The last if statment checks the last loop, if current indice `i` is the last element of the list, and `end_i` is less than equal to `i`. And we add elements to the hashmap_arr accordingly.

## Complexity
- Time complexity: $$O(n)$$
  Since we are using a single loop the time complexity is $$O(n)$$

- Space complexity: $$O(1)$$
  Since we are using 2 pointers and a list which does not grow according to the size of the input list, we are using $$O(1)$$ space complexity.

#### Code - Python
```python3 []
class Solution:
	def summaryRanges(self, nums: list[int]) -> list[str]:
		hashmap_arr = []

		# If length is 0
		if len( nums ) == 0:
			return hashmap_arr

		if len( nums ) == 1:
			return [str(nums[0])]

		# initiate window
		start_i = 0
		end_i = 0
		for i in range( 1, len( nums ) ):
			# if consecutive items in the list are in range , AND its not the last number of the list.
			if nums[i] - nums[end_i] ==  1 and (i + 1) < len( nums ):
				end_i = i
				continue
			# If consecutive numbers are not in range. Add the previous range to the hashmap.
			elif nums[i] - nums[end_i] > 1:
				if end_i == start_i:
					hashmap_arr.append( str( nums[end_i] ) )
				else:
					hashmap_arr.append( str( nums[start_i] ) + "->" + str( nums[end_i] ) )
				start_i = i
				end_i = i

			# in the last loop, check if there are any numbers left in nums to be checked.
			if (i + 1) >= len( nums ) and end_i <= i:
				if end_i == len( nums ) - 1:
					hashmap_arr.append( str( nums[len(nums)-1] ) )
				else:
					hashmap_arr.append( str( nums[start_i] ) + "->" + str( nums[len(nums)-1] ) )

		return hashmap_arr

```

# *Please UpVote, gives me encouragement. :-)*