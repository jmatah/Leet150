# 205. Isomorphic Strings

## Intuition
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Approach
My approach to the problem would be to creat two hashmaps `arr` and `arr_rev`. One for `s` to `t`. And another hashmap to map characters from `t` to `s`. I would tackle this in a single pass.

Since we need a two way check, we have a single loop, with 2 if statements.

The first if statement checks if the current character in `s` is already in `arr`, and if yes then the value stored in the hashmap `rev` is the same as the current value of `t`. Else assign to `arr`.

The second if statement reverse checks if the current character in `t` is already in `arr_rev`, and if yes then the value stored in the hashmap `arr_rev` is the same as the current value of `s`. Else assign to `arr_rev`.

For E.g. the the result of the approach would be for `s = "egg"` and `t = "add"`, `arr` would be: `{ "e": "a", "g": "d" }`

and `arr_rev` would be the opposite of arr for the second pass, which compares `t` to `s` would be: `{ "a": "e", "d": "g" }`

## Complexity
- Time complexity: $$O(n)$$
  Since we have a single loop, the time complexity would be $$O(n)$$.

- Space complexity: $$O(1)$$
  We do have 2 hashmaps, but the max they can grow is to 127, as the contraint is they can contain any valid ASCII character. And would not grow linearly in size according to input.

#### Python 3
```python3 []
class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		arr = {}
		arr_rev = {}
		for i in range( 0, len( s ) ):
			if s[i] in arr and arr[s[i]] != t[i]:
				return False
			else:
				arr[s[i]] = t[i]

			if t[i] in arr_rev and arr_rev[t[i]] != s[i]:
				return False
			else:
				arr_rev[t[i]] = s[i]
		return True

```

## *Please UpVote, Gives me encouragement :-)*