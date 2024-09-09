# LeetCode 1 - Two Sum - Solution

## Intuition
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

I would approach this problem with a hashmap.

## Approach
Iterate throught `nums` and check whether the result of subtrating the target from the current value `num` is present in the hashmap `hash_arr`. If we have the result, then the current indice and the result is the answer. Else we add the current value and indice to the hashmap `hash_arr`. 

The logic is if `x + y = z` ~= `z - x = y`. So subtracting the target from the current iterative value, should give us the resultant other value's indice.

## Complexity
- Time complexity: $$O(n)$$
  Since we only have one single loop, the time complexity as worst case is $$O(n)$$

- Space complexity: $$O(n)$$
  As we are using a hashmap, which will grow according to the length of `nums`, and in worst case will almost by the length of `nums`, we will be using space complexity as $$O(n)$$.

#### Python
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(0, len( nums ) ):
            if target - nums[i] in num_dict:
                return [i, num_dict[target - nums[i]]]
            else:
                num_dict[nums[i]] = i
        return False
```

# *Please UpVote, gives me encouragement :-)*