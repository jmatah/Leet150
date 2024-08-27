class Solution:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		i = 0
		strs_word = strs[i]
		i += 1
		while i < len( strs ):
			curr = strs[i]
			while strs_word.startswith( curr ) == False:
				curr = curr[:-1]
			strs_word = curr
			i += 1
		return strs_word

sol = Solution()

strs = ["flower","flow","flight","flowed","fight"]
longest = sol.longestCommonPrefix( strs )
print( longest )

			