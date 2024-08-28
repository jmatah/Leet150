# 28. Find the Index of the First Occurrence in a String

## Intuition
We are given two strings `needle` and `haystack`, and we need to return the `index` of the first occurrence of `needle` in `haystack`, or `-1` if needle is not part of haystack. 

## Approach
First we check for empty haystack, empty needle and a scenario where the length of haystack is smaller than the length of the needle. and return `-1`. 

Then we run the Pythons inbuilt function `find()`, which gives is `i` the start index of the `needle`, or a `-1` if it does not find the `needle` in the `haystack`

If a match is found, return the starting index `i`.
If no match is found after the loop completes, return `-1`.

## Complexity
- Time complexity: $$O(n)$$
  The built in function `find()` has a time complexity is $$O(n)$$. And for worst cases, i would assume $$O(m*n)$$, as internally `find()` compares each character of the `needle` to the `haystack`.

- Space complexity: $$O(1)$$
  We are not using any other data structure so Space complexity is $$O(1)$$.

#### Python
``` python []
class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if len( haystack ) == 0:
			return -1
		if len( needle ) == 0:
			return -1
		if len( haystack ) < len( needle ):
			return -1

		j = haystack.find( needle )
		return j
```