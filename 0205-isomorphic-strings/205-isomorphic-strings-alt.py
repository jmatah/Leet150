class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		arr = {}
		for i in range( 0, len( s ) ):
			if s[i] in arr and arr[s[i]] != t[i]:
				return False
			else:
				arr[s[i]] = t[i]

			k = arr.keys()
			v = arr.values()
			found = list(k)[list(v).index(t[i])]
			if t[i] in v and found != s[i]: 
				return False

		return True

sol = Solution()

s = "paper"
t = "title"

isIsomorphic = sol.isIsomorphic( s, t )
print( "final: ", isIsomorphic )


            
            