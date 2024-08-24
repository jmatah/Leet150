"""
# 13. Roman to Integer
Easy Solution | O(n) | Single Pass | Python | Dictionary | Explaination

## Intuition
Given a string in roman numeral, we need to convert it to a decimal numeral. Keeping in mind that anything followed by I,X, C acts differently, coz these are subtracted with the next number. For E.g. III make become 3, but if the next number is higher E.g. IV or IX it becomes 4 and 9 respectively.

## Approach
The approach taken here is a single pass over the string from left to right, and look for conditions where numbers may need to be subtracted instead of being added.

The loop will go through each alphabet i, and compare it with the next alphabet i+1, if found the loop will subtract element at n+1 with i and then ad it to total; And here increament the counter i by an additional 1 coz we have processed that character as well. Else it will just add i with the total. In the end increament i by 1
Complexity

## Time complexity: O(n)
Coz we are taking a single pass with all elements in the string.

## Space complexity: O(1)
Since we are only using pointer variables and a data dictionary, not related to the input at hand.
"""
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

