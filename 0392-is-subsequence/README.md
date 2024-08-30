# LeetCode: 329 - Is Subsequence - Solution

## Intuition
Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise. The **Subsequence** would mean the order of characters in the subsequence `s` appear in the same sequence and not necessarily contigiously in the string `t`.

## Approach
To find the subsequence `s` in the string `t` we would take two pointers `index_s` for `s` and `index_t` for string `t`. 

We would then iterate through string `t` with `index_t` and compare each alphabet lenearly, and incease the pointer `index_s` as and when we come across a character in the subsequence string `s`.

If the result `index_s` is equal to the length of the subsequence `s` which means we have found the complete subsequence `s`.

If `s` or `t` is None/ Null we return `false`. If the length of `s` and `t` is `0` we return `true`.

## Complexity
- Time complexity: $$O(n)$$
  Since we are iterating through `t` once the Time complexity would be $$O(n)$$.

- Space complexity: $$O(1)$$
  We are not using any data structure in our program just two variables, so our Space complexity is $$O(1)$$.

#### Python
```python3 []
class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		index_s = 0
		if s == None or t == None:
			return False
		if len( s ) == 0 and len( t ) == 0:
			return True
		
		for index_t in range( 0, len( t ) ):
			if index_s < len(s) and t[index_t] == s[index_s]:
				index_s += 1

			if index_s == len(s):
				break

		if index_s == len(s):
			return True
		else:
			return False
            
```
# *Please UpVote, gives me encouragement :-)!*