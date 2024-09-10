class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap_arr = {}

        while True:
            summ = 0
            x = [int(d) for d in str(n)]
            print(x)
            for k in x:
                summ += ( k ** 2 )
                print( k, ( k** 2 ), summ )

            if summ in hashmap_arr:
                return False
            
            if summ == 1:
                return True
            
            n = summ
            hashmap_arr[summ] = 1

sol = Solution()
n = 13775

ret = sol.isHappy( n )
print( ret )

