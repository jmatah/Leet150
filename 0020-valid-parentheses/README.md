# LeetCode - 20. Valid Parentheses - Python Solution

## Intuition
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

 - Open brackets must be closed by the same type of brackets.
 - Open brackets must be closed in the correct order.
 - Every close bracket has a corresponding open bracket of the same type.

This problem would be best solved by a stack using a list, adding open braces, and popping closed ones. So the end the stack should be empty.


## Approach
I would create a hashmap with a dictionay object `braces` of open and closed braces, with closed braces as keys, so we know which open brace to search for.

Then i would create a list `stack_arr` which will store all instances of open parenthesis. And pop from the stack, when a closed parenthesis is encountered. This provided the stack is not empty.

In the end if the stack is not empty, and there are some items left, we know that there are still some open parenthesis, and the string is not valid. 

## Complexity
- Time complexity: $$O(n)$$
  As we are running a single loop through string `s`, our time complexity is $$O(n)$$.

- Space complexity: $$O(n)$$
  The space complexity of the stack we are using would be at max $$O((1/2) n)$$, since we are only storing opening parenthesis 
  But since we dont use constants the spce complexity would be $$O(n)$$.

#### Code - Python
```python3 []
class Solution:
	def isValid(self, s: str) -> bool:
		if len( s ) < 1:
			return False
		
		if ( len( s ) % 2 ) == 1:
			return False

		braces = {
				']': '[',
				'}': '{',
				')': '(',
			}
		
		stack_arr = []
		last_closed = None
		
		for i in range( 0, len( s ) ):
			if s[i] in list(braces.values()):
				stack_arr.append( s[i] )
			elif s[i] in list(braces.keys()) and len( stack_arr ) > 0:
				last_closed = stack_arr.pop()
				if last_closed != braces[ s[i] ]:
					return False
			else:
				return False
			
		if len( stack_arr ) != 0:
			return False
		return True
	
```

# *Please UpVote, gives me encouragment :-)*
