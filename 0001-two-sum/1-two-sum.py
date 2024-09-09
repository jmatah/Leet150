class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i in range(0, len( nums ) ):
            num = nums[i]
            print( i, num, num_dict )
            if target - num in num_dict:
                return [i, num_dict[target - num]]
            else:
                num_dict[num] = i
        return False

sol = Solution()

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

nums = [2,7,11,15]
target = 9

ret = sol.twoSum( nums, target )
print(ret)
