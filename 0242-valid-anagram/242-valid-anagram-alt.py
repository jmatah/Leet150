class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len( s ) != len( t ):
			return False

		s1 = list(s)
		t1 = list(t)
		s1.sort()
		t1.sort()

		print(s1, t1)
		if s1 == t1:
			return True
		else:
			return False

sol = Solution()

s = "anagram"
t = "nagaram"

#s = "rata"
#t = "tara"

ret = sol.isAnagram( s, t )
print(  ret )
