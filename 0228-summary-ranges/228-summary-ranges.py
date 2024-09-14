class Solution:
	def summaryRanges(self, nums: list[int]) -> list[str]:
		hashmap_arr = []

		# If length is 0
		if len( nums ) == 0:
			return hashmap_arr

		if len( nums ) == 1:
			return [nums[0]]

		# initiate window
		start_i = 0
		end_i = 0
		for i in range( 1, len( nums ) ):
			# if consecutive items in the list are in range , AND its not the last number of the list.
			if nums[i] - nums[end_i] ==  1 and (i + 1) < len( nums ):
				end_i = i
				continue
			# If consecutive numbers are not in range. Add the previous range to the hashmap.
			elif nums[i] - nums[end_i] > 1:
				if end_i == start_i:
					hashmap_arr.append( str( nums[end_i] ) )
				else:
					hashmap_arr.append( str( nums[start_i] ) + "->" + str( nums[end_i] ) )
				start_i = i
				end_i = i

			# in the last loop, check if there are any numbers left in nums to be checked.
			if (i + 1) >= len( nums ) and end_i <= i:
				if end_i == len( nums ) - 1:
					hashmap_arr.append( str( nums[len(nums)-1] ) )
				else:
					hashmap_arr.append( str( nums[start_i] ) + "->" + str( nums[len(nums)-1] ) )

		return hashmap_arr

sol = Solution()

nums = [0,1,2,4,5,7]
# nums = [-4,0,2,3,4,6,8,9]
nums = [-1]
print(nums)

ret = sol.summaryRanges( nums )
print( ret )
