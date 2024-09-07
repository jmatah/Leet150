class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		hashmap_s = {}
		hashmap_t = {}
        
		if len( s ) != len( t ):
			return False

		for i in range( 0, len( s ) ):
			if s[i] in hashmap_s:
				hashmap_s[s[i]] += 1
			else:
				hashmap_s[s[i]] = 1

		for i in range( 0, len( t ) ):
			if t[i] in hashmap_t:
				hashmap_t[t[i]] += 1
			else:
				hashmap_t[t[i]] = 1

		print( hashmap_s, hashmap_t)
		if hashmap_s == hashmap_t:
			return True
		else:
			return False

sol = Solution()

s = "anagram"
t = "nagaram"

s = "rata"
t = "tara"

ret = sol.isAnagram( s, t )
print(  ret )
