class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		hashmap = {}
		for i in magazine:
			if i in hashmap:
				hashmap[i] += 1
			else:
				hashmap[i] = 1

		for i in ransomNote:
			if i in hashmap and hashmap[i] > 0:
				hashmap[i] -= 1
			else:
				return False
		
		return True

sol = Solution()
ransomNote = "aba"
magazine = "aab"
ret = sol.canConstruct( ransomNote, magazine )
print( 'final: ', ret )