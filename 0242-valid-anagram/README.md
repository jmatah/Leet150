# 242. Valid Anagram

## Intuition
Given two strings `s` and `t`. Return `true` if `t` is an `anagram` of `s`, and `false` otherwise.

## Approach
There are 2 aproaches we can take, the first intuition is to have 2 hashmaps, and compare them. The time complexity here would be $$O(m+n)$$. Where `len(n)` == `len(m)` so $$O(2n)$$ or simply $$O(n)$$.

The second apporach, and a very pythonic way of apporaching this problem would be to convert `s` and `t` to lists, `sort()` them and compare them. The time complexity of `sort()` is $$O(nlog(n))$$ and $$O(mlog(m))$$. So $$O(nlog(n) + mlog(m)))$$, where `len(n)` == `len(m)` so $$O(2(nlog(n)))$$ or simply $$O(nlog(n))$$.

## Complexity
- Solution 1: Create `hashmaps`
  - Time complexity: $$O(n)$$

  - Space complexity: $$O(1)$$
  Since we are creating two hashmaps, of lower case english characters, the space complexity does not grow with `n`. So space complexity is $$O(1)$$

- Solution 2: Convert to `list()`
  - Time Complexity: $$O(nlog(n))$$

  - Space complexity: $$O(n)$$
  A string in Python is an iterable of characters. When you perform list(s), Python creates a new list where each character from the string s becomes an individual element in the list. 

#### Python
```python-Solution1 []
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		hashmap_s = {}
		hashmap_t = {}
        
		if len( s ) != len( t ):
			return False

		for i in range( 0, len( s ) ):
			if s[i] in hashmap_s:
				hashmap_s[s[i]] += 1
			else:
				hashmap_s[s[i]] = 1

		for i in range( 0, len( t ) ):
			if t[i] in hashmap_t:
				hashmap_t[t[i]] += 1
			else:
				hashmap_t[t[i]] = 1

		if hashmap_s == hashmap_t:
			return True
		else:
			return False
```
```python-Solution2 []
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len( s ) != len( t ):
			return False

		s1 = list(s)
		t1 = list(t)
		s1.sort()
		t1.sort()

		if s1 == t1:
			return True
		else:
			return False
```

# *Please UpVore, Gives me Encouragement :-)*