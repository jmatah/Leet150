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
