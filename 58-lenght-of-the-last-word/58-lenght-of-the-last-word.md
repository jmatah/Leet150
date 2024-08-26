# LeetCod: 58 - Lenght of the last word - Solution

## Intuition
Th Problem given is a string, and we need to find the ength of the last word in the string. E.g. `How are you` should return `3`, as the last word is `you`, with length `3`.

## Approach
The first approach that comes to mind is a reverse for loop, and search for the first space, after the first non-space character. This would skip any spaces at the end of the string. Since we have a loop time complexity and space complexity are both at $$O(n)$$.

We can also use inbuilt functions, without compromising giving a good solution. We strip the given string, the we use `split()` without an arguement to split the string into words. Then we get the last word and return the length with the `len` function. The inbuilt function `split()` also has a time complexity and space complexity of $$O(n)$$ where `n` is the length of the string, since the function iterates through each character.

Do remember when we split the string the result is a `list`. And when we get the last word, with `s[-1:]` we get the last element as a single element as a `list`. We then want the first element of the we do `s[-1:][0]`.

## Time complexity: $$O(n)$$
  The built in function `split()` has time complexity of $$O(n)$$.

## Space complexity: $$O(n)$$
  The built in function `split()` has space complexity of $$O(n)$$.

#### Python3
```python []
class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		s = s.strip()
		s = s.split()
		last_s = s[-1:][0]
		return len( last_s )
```
