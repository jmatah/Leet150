""""
# Intuition
The Problem states we are given a sorted array, and we need to remove dupicate values from the array `in-place`. We need to return the number of unique elements `k`.

# Approach
The approach is to iterate over the array, and compare and assign to the current position, the values not equal to the next position. IF the value is unequal we assign it to the current position held in variable `k`, and increase `k`. We return the value of `k + 1` as the result as `k` is the index value.

By iterating the whole array once, we avoid any extra space, and solve the problem with Time complexity of O(n).

# Complexity
- Time complexity: O(n).
- Space complexity: O(1)
"""
class Solution:
	def removeDuplicates(self, nums: list[int]) -> int:
		k = 0
		for i in range( 1, len(nums) ):
			if nums[k] != nums[i]:
				k += 1
				nums[k] = nums[i]

		return k + 1

sol = Solution()

nums = [1,1,2]
expectedNums = [1,2,2]

print(nums)
k = sol.removeDuplicates(nums)
print(nums)
print('final: ', k)

if k == len( expectedNums ):
	print( "all good" )

i = 0
for i in range( 0, len(nums) ):
	if nums[i] != expectedNums[i]:
		print( 'Not equal', i, nums[i], expectedNums[i] )
		break
