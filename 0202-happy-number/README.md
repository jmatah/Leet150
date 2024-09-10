# LeetCode: 202 - Happy Number - Python Solution

## Intuition
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

 - Starting with any positive integer, replace the number by the sum of the squares of its digits.
 - Repeat the process until the number equals `1` (where it will stay), or it loops endlessly in a cycle which does not include `1`.
 - Those numbers for which this process ends in `1` are happy.

Return `true` if n is a happy number, and `false` if not.

I would take is create a hashmap for the result of each loop, so we can track and compare if we have the result already. I would use a `dict` to create a hashmap.

## Approach
The Approach I woudl take is create a hashmap of the sum of every iteration so if we have the same sum we need to quit the loop. For the loop itself, I would use an infinite loop as I don't know when the loop will end. 

There are only two conditions where the infinite loop will end:
 - When the result is `1`, it returns True, as it is regarded as a happy number.
 - When we get a result which is present in the hashmap, as we have got this result previously.

## Complexity
- Time complexity: $$O(n)$$
  Even though this is an infinite loop, but we have 2 conditions where it breaks the loop. So the time complexity in worst case would be $$O(n)$$

- Space complexity: $$O(n)$$
  We are using a hashmap, which in worst case, would be $$O(n)$$.

#### Python
```python3 []
class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap_arr = {}

        while True:
            summ = 0
            # Convert Int to List.
            x = [int(d) for d in str(n)]

            # Get sum of squares.
            for k in x:
                summ += ( k ** 2 )

            if summ in hashmap_arr:
                return False
            
            if summ == 1:
                return True
            
            n = summ
            hashmap_arr[summ] = 1

```