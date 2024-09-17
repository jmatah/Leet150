from typing import Optional 

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

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

	def append( self, data ):
		new_node = ListNode()
		new_node.val = data

		if self.head == None:
			self.head = new_node
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = new_node

	def printList( self ):
		tmp = self.head
		print(' ')
		while tmp:
			print( tmp.val, end=", " )
			tmp = tmp.next

list1 = [1,2,4]
list2 = [1,3,4]
list1 = []
list2 = []

list1 = []
list2 = [0]

sol1 = Solution()
for i in list1:
	sol1.append( i )
sol1.printList()

sol2 = Solution()
for i in list2:
	sol2.append( i )
sol2.printList()

sol3 = Solution()
sol3.head = sol3.mergeTwoLists( sol1.head, sol2.head )
print('Final: ')
sol3.printList()

