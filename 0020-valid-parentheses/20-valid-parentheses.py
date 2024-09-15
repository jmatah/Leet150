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
	
sol = Solution()

s = "{()[]}"
s = "()[]{}"
s = "(]"
s = "([])"
s = "(("
s = "})"
s = "{(})"
s = "{"
ret = sol.isValid( s )
print( ret )
