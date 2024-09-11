class Solution:
	def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
		hashmap_arr = {}
		for i in range( 0, len( nums ) ):
			if nums[i] in hashmap_arr and abs( i - hashmap_arr[ nums[i] ] ) <= k:
				return True
			else:
				hashmap_arr[nums[i]] = i
		return False

sol = Solution()

nums = [1,2,3,1]
k = 3
# nums = [1,0,1,1]
# k = 1

# nums = [1,2,3,1,2,3]
# k = 2

ret = sol.containsNearbyDuplicate( nums, k )
print( ret )
