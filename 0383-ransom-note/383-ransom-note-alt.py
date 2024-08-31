"""
Single Loop;
Time Complexity: O(m + n + nlog(n) )
Space Complexity: O( m + n )
"""

class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		hashmap = {}
		added = []

		for i in ransomNote:
			if i in magazine:
				if not i in added:
					hashmap[i] = magazine.count(i)
					added.append(i)

			# Process Note:
			if i in hashmap:
				hashmap[i] -= 1
			else:
				hashmap[i] = -1

		hashmap_list = list(hashmap.values())
		hashmap_list.sort()
		if hashmap_list[0] >= 0:
			return True
		else:
			return False

sol = Solution()
ransomNote = "a"
magazine = "b"

ransomNote = "aa"
magazine = "aba"
ret = sol.canConstruct( ransomNote, magazine )
print( 'final: ', ret )