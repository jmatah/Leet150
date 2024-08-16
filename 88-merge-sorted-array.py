"""
 # Intuition
We are given two sorted arrays nums1 and nums2, in non decreasing orders, and 2 numbers m and n. Where m and n are elements we need to merge from the two arrays. The length of nums1 = m+n and length of nums2 is n. We need to merge the two already sorted arrays and the result should be stored in nums1.

# Approach
We can use 2 pointers, and start merging from the i'th and j'th position of the arrays, where i = m - 1 and j = n - 1, and we use another pointer k where k = m + n - 1 to store where the larger element will be placed. We compare the elements in nums1 and nums2 and place the larger element in nums1 at the kth element. We keep doing this till j >= 0. For the remaining elements in nums1, we don't do anything as they are already sorted.

# Complexity
- Time complexity: O(m+n)
`We iterate through both the arrays once so time complexity is O(m+n)`

- Space complexity: O(1)
`We are not using any extra space so space complexity is O(1)`
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:] = nums1[:(m+n)] + [0] * ( (m+n) - len( nums1 ) )
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if ( i >= 0 and nums1[i] > nums2[j] ):
                nums1[k] = nums1[i]
                i -= 1
            else:
                print( 'inside: ', k, i, j, nums1[i], nums2[j] )
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1

"""
Note:
Because everything in Python is an object, when doing nums1 = sorted(nums1[:m] + nums2[:n]) two things happen:

    a new object is created which is the result of sorted(nums1[:m] + nums2[:n]), while the original nums1 that was passed in to the function remains untouched
    So the line nums1 = sorted(nums1[:m] + nums2[:n]) is actually equivalent to nums1 = new object, i.e. the address of new object is now assigned to nums1

But since the problem requires modifying the original object nums1, you get an error.
However, when using nums1[:], you fill up the indices of the original nums1 with new values, so the original nums1 is indeed sorted by the end.
"""
sol = Solution()

nums1 = [1,2,3,4,0,0]
m = 3
nums2 = [6,7,8]
n = 3
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)


nums1 = [0]
m = 0
nums2 = [1]
n = 1
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)
