# 125. Valid Palindrome - Python Solution

## Intuition
Given a string we ehave to check whether the string is a Pallendrome or not. A Pallendrome is a string which is read the same way from left to right , as well from right to left. E.g. `Madam`.

For the problem we need to remove all non-alhpa numeric characters from the string, convert them to lowercase, and then compare if the resultant string is pallendrome in nature or not.

## Approach
The approach I will take is a two pointer approach, one will start from the begining for the string `l`, and the other from the last character of the string `r`. 

We will start a while loop till `l` is less than `r`. Coming inwards, first we skip all non-alphanumeric characters on the left, then on the right.

Then we compare current pointer locations if the two characters are equal, if yes, we proceed with incrementing left `l`, and right `r`. and repeat the loop. If they are not equal, we bail, coz the string is not of pallendromic nature.

## Complexity
- Time complexity: $$O(n)$$
  Since we have a loop through the string once, our time complexity is $$O(n)$$

- Space complexity: $$O(1)$$
  Since we are not using any extra space to get to an answer, our space complexity is $$O(1)$$.

#### Python
```python3 []
class Solution:
	def isPalindrome(self, s: str) -> bool:
		l, r = 0, len(s) - 1
		while l < r:
			while l < r and not ( s[l].isalpha() or s[l].isnumeric() ):
				l += 1

			while l < r and not ( s[r].isalpha() or s[r].isnumeric() ):
				r -= 1

			if s[l].lower() != s[r].lower():
				return False
			l, r = l+1, r-1
		return True
```

# *Please UpVote, Gives me Encouragement :-)*