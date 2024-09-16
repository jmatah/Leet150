# Leetcode - 141. Linked List Cycle - Python Solution with test cases.

## Intuition
Given is the `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

My intuition would be to solve this problem with the Floyd's Tortoise and Hare algorithm (also called the two-pointer technique or the slow and fast pointer). The slow pointer moves one step, and the fast pointer moves two step at a time.

If the linked list has no cycle, the fast pointer will eventually reach the end.

If the linked list has a cycle, given that the fast pointer moves twice as fast, the fast pointer will eventually meet the slow pointer at some node from behind.

## Approach
To approach the problem we can use the Floyd's Tortoise and Hare algorithm (also called the two-pointer technique or the slow and fast pointers). The slow pointer moves one step at a time, and the fast pointer moves 2 steps at a time.

If the list has no cycle, the `fast` pointer will reach the node where the `next` is `null`.

If the list has a cycle, then eventually the `fast` will meet the `slow` from behind since the `fast` pointer moves twice as fast as the `slow` one. We run the loop till `slow != fast`, and break if `fast` is `None` or `fast.next` is `None`. Else we advance the two pointers accordingly.

## Complexity
- Time complexity: $$O(n)$$
  The time complexity is $$O(n)$$ where n is the number of nodes in the linked list. In case of no cycle, the loop will run through all then nodes. If there is a cycle, the loop will run till `fast == slow` with a single pass over the nodes.

- Space complexity: $$O(1)$$
  The space complexity is $$O(1)$$ as we are using only 2 pointers regardles of th size of the linked list, which means we only require a constant amount of space.

#### Code - Python
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		if head == None or head.next == None:
			return False

		slow = head
		fast = head.next
		
		while slow != fast:
			if fast == None or fast.next == None:
				return False
			
			slow = slow.next
			fast = fast.next.next
		return True
```

# *Please UpVote, Gives me encouragement. :-)*