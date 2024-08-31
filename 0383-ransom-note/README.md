# LeetCode: 383. Ransom Note - Solution

## Intuition
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

## Approach
The first thing that comes to mind using `counter()`. The internal time complexity of `collection.counter()` is $$O(n)$$. So might as well use our own. We iterate through `magazine` and create a hashmap, with $$O(n)$$. Then we iterate through `ransomeNote` checking if the given character exists. Subtracting each character with `1` everytime.

## Complexity
- Time complexity: $$O(n+m)$$
  We are iterating through `magazine` and then through `ransomeNote`, so worst case is $$O(m+n)$$.

- Space complexity: $$O(n)$$
  We are creating a hashmap of size `magazine`, so extra space we are using is $$O(n)$$

#### Python3
```python []
class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		hashmap = {}
		for i in magazine:
			if i in hashmap:
				hashmap[i] += 1
			else:
				hashmap[i] = 1

		for i in ransomNote:
			if i in hashmap and hashmap[i] > 0:
				hashmap[i] -= 1
			else:
				return False
		
		return True
```
