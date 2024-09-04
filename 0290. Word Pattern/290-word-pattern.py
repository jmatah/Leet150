class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		hashmap_pattern = {}
		hashmap_s = {}

		s = s.strip()
		s = s.split()

		if len( s ) != len( pattern ):
			return False

		for i in range( 0, len( s ) ):
			if s[i] in hashmap_s and hashmap_s[s[i]] != pattern[i]:
				return False
			else:
				hashmap_s[s[i]] = pattern[i]
			if pattern[i] in hashmap_pattern and hashmap_pattern[pattern[i]] != s[i]:
				return False
			else:
				hashmap_pattern[pattern[i]] = s[i]
		return True

sol = Solution()

pattern = "abba"
s = "dog cat cat dog"

pattern = "abba"
s = "dog cat cat fish"

pattern = "baba"
s = "dog cat cat dog"

ret = sol.wordPattern( pattern, s )
print('Final: ', ret )




