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

sol = Solution()

s = "egg"
t = "add"

isIsomorphic = sol.isIsomorphic( s, t )
print( "final: ", isIsomorphic )


            
            