# LeetCode: 21. Merge Two Sorted Lists - Python Solution with Tests

## Intuition
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

The advantage we have is the two linked list are already sorted, so we take advantage and implement a recursive function to merge the two.

## Approach
We merge the two already sorted linked list, by a recursive function. For input we have 2 lists `list1` and `list2`, and we compare the current `val` at both linked list, if `list1` is less we call the same function recursively with `list1.next`, and `list2`. Else we call the same function recursively with `list1` and `list2.next`. In both cases we send back the list with the smaller value.

The recursion ends with either of the linked list reach their end, then we send back the other list.

Calling the function recursively, we merge the two linked list.

## Complexity
- Time complexity: $$O(m+n)$$
  We are using a recursive function, and the function is being called till the elements of both linked list are merged, so $$O(m+n)$$

- Space complexity: $$O(1)$$
  We are not using any other variable the space complexity is $$O(1)$$.

#### Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def __init__( self ):
		self.head = None
        
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if list1 == None:
			return list2

		if list2 == None:
			return list1

		tmp = None
		if list1.val < list2.val:
			tmp = list1
			tmp.next = self.mergeTwoLists( list1.next, list2 )
		else:
			tmp = list2
			tmp.next = self.mergeTwoLists( list1, list2.next )
		return tmp

```

# *Please UpVote, gives me encuragement :-)*