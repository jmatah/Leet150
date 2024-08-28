class Solution:
	def removeElement(self, nums: list[int], val: int) -> int:
		count = 0
		for i in nums:
			if i != val:
				nums[count] = i
				count += 1

		return count

nums = [3,2,2,3]
val = 3
expectedNums = [2,2,2,3]


sol = Solution()
k = sol.removeElement(nums, val)
print(nums)

if k != 2:
	print('Not equal')

nums.sort()
for i in nums:
	if nums[i] != expectedNums[i]:
		print('print not equal: ', i, nums[i], expectedNums[i] )
		break

