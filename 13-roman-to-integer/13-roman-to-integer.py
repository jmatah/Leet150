class Solution:
	def romanToInt(self, s: str) -> int:
		data = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000,
		}

		prev, curr, total, i = 0, 0, 0, 0
		letter = [x for x in s]
		while i < len( letter ):
			if i+1 < len(letter) and data[letter[i]] < data[letter[i+1]]:
				total += data[letter[i+1]] - data[letter[i]]
				i += 1
			else:
				total += data[letter[i]]

			i += 1
		return total

sol = Solution()


print('--==--')
str = 'III'
cur = sol.romanToInt( str )
print(cur)
print('3 --==--')

str = 'IV'
cur = sol.romanToInt( str )
print(cur)
print('4 --==--')

str = 'CMLII'
cur = sol.romanToInt( str )
print(cur)
print('952--==--')

str = 'LVIII'
cur = sol.romanToInt( str )
print(cur)
print('58--==--')

str = "MCMXCIV"
cur = sol.romanToInt( str )
print(cur)
print('1994--==--')

