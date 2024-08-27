# LeetCode: 14 - Longest common prefix - Solution

## Intuition
The prolem gives us a list of words in an array, and we need to find the longest common prefix string. The problem is to compare the first word with the rest of the words one at a time, to check the first common characters, each time. 

## Approach
We assign the first words to `strs_word` and then do a while loop to compare each word to `strs_word`. We have an inner loop with the length of the second word, decreasing its length by one on each comparison. The moment we find the prefix, we assign the prefix to `strs_word` and `break` to start on the next word.

## Complexity
- Time complexity: $$O(n+m)$$
  We have an outer loop of words and a inner loop on the length of each consecutive word. Hence, the Time complexity is $$O(m+n)$$

- Space complexity: $$O(m)$$ 

#### Python 3
```python []
class Solution:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		i = 0
		strs_word = strs[i]
		i += 1
		while i < len( strs ):
			curr = strs[i]
			while strs_word.startswith( curr ) == False:
				curr = curr[:-1]
			strs_word = curr
			i += 1
		return strs_word
```