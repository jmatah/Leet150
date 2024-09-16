from typing import Optional

class ListNode:
	def __init__(self, value=0, next=None):
		self.val = value
		self.next = next

class Solution:
	def __init__( self ):
		self.head = None

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

	def append( self, data ):
		new_node = ListNode( data )

		if self.head == None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next

		last.next = new_node

	def printList(self):
		tmp = self.head
		print('')
		while( tmp ):
			print( tmp.val, end=", ")
			tmp = tmp.next
	
	# Helper function to create a cycle in the linked list
	def createCycle( self, pos:int ):
		if pos == -1:
			return self.head
		cycle_node = None
		current = self.head
		tail = None
		index = 0
		
		while current:
			if index == pos:
				cycle_node = current
			tail = current
			current = current.next
			index += 1
		
		if tail:
			tail.next = cycle_node
		
		return self.head

sol = Solution()

# Test Case 1
head = [3,2,0,-4]
pos = 1

# Test Case 2
head = [1,2]
pos = 0

# Test Case 3
head = [1]
pos = -1

# Test Case 4
head = [1]
pos = None

# Test Case 5
head = [1,2,3,4,5]
pos = 1

for i in range( 0, len( head ) ):
	sol.append( head[i] )

sol.printList()
sol.createCycle( pos )  # Creates a cycle at index `pos`

sol2 = Solution()
ret = sol2.hasCycle(sol.head)
print(ret)
