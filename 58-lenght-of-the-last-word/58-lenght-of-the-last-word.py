class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		s = s.strip()
		s = s.split()
		last_s = s[-1:][0]
		return len( last_s )

sol = Solution()

str = "Hey, how are you"
a = sol.lengthOfLastWord( str )
print( str, a )

str = "Hey, how are you ?"
a = sol.lengthOfLastWord( str )
print( str, a )

str = "Hey, how are you?"
a = sol.lengthOfLastWord( str )
print( str, a )

str = "Hey, how are you?  "
a = sol.lengthOfLastWord( str )
print( str, a )

