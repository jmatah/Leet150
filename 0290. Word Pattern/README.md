# 290. Word Pattern | 2 hashmaps | Python | O(n)  | Single pass | Explaination

## Intuition
The Problem given is a pattern `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`. Specifically.

- Each letter in `pattern` maps to exactly one unique word in `s`.
- Each unique word in `s` maps to exactly one letter in `pattern`.
- No two letters map to the same word, and no two words map to the same letter.

## Approach
To solve this problem we create 2 hashmaps `hashmap_s` and `hashmap_pattern`, to ensure one-to-one relationship (bijection) between `s` and `pattern`. I would iterate once to the count of words in string `s` and check both hashmaps.

## Complexity
- Time complexity: $$O(n)$$
  Since we have only one for loop, therefor the time complexity is $$O(n)$$.

- Space complexity: $$O(1)$$
  Since we are using 2 hashmaps, but thos hashmaps ar not growing in in respect to `s`. `s` has only lowercase english letters. So the max size of both hashmaps is 26. So the space complexity is independant of the input, hence $$O(1)$$. 

#### Python
```python3 []
class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		hashmap_pattern = {}
		hashmap_s = {}

		s = s.strip()
		s = s.split()

		if len( s ) != len( pattern ):
			return False

		for i in range( 0, len( s ) ):
			if s[i] in hashmap_s and hashmap_s[s[i]] != pattern[i]:
				return False
			else:
				hashmap_s[s[i]] = pattern[i]
			if pattern[i] in hashmap_pattern and hashmap_pattern[pattern[i]] != s[i]:
				return False
			else:
				hashmap_pattern[pattern[i]] = s[i]
		return True
```

# *Please UpVote, gives me encouragement*