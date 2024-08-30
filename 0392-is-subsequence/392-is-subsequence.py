class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		index_s = 0
		if s == None or t == None:
			return False
		if len( s ) == 0 and len( t ) == 0:
			return True
		
		for index_t in range( 0, len( t ) ):
			if index_s < len(s) and t[index_t] == s[index_s]:
				index_s += 1

			if index_s == len(s):
				break

		if index_s == len(s):
			return True
		else:
			return False

sol  = Solution()
s = "abcx"
t = "ahbgdc"

s = "abcxc"
t = "axhbgdcxc"

is_subs = sol.isSubsequence( s, t )
print( 'Is Subs: ', is_subs ) 