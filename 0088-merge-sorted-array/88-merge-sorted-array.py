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
