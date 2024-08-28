class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if len( haystack ) == 0:
			return -1
		if len( needle ) == 0:
			return -1
		if len( haystack ) < len( needle ):
			return -1

		j = haystack.find( needle )
		return j

sol = Solution()

haystack = "sadbutsad"
needle = "sad"

haystack = "leetcode"
needle = "leeto"


haystack = "matahjatin"
needle = "jatil"

find = sol.strStr( haystack, needle )
print('final: ', find )
