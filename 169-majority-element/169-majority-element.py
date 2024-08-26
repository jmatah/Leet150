class Solution:
	def majorityElement(self, nums: list[int]) -> int:
		hashmap = {}

		for i in nums:
			hashmap[i] = hashmap.get(i, 0) + 1
			if hashmap[i] > len( nums )// 2:
				return i

		return -1

sol = Solution()

arr = [2,2,1,1,1,2,2]
cnt = sol.majorityElement( arr )
print(cnt)