class Solution:
	def isPalindrome(self, st: str) -> bool:
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

sol = Solution()
s = "A man, a plan, a canal: Panama"
# s = "race a car"
#s = "0P"

ret = sol.isPalindrome( s )
print( "Return ", ret )