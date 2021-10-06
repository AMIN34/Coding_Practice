"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

# Method 1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Base Cases
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        
		#Starting node for the merged list
        if l1.val<=l2.val:
            head=l1
            new=l1
            l1=l1.next
        else:
            head=l2
            new=l2
            l2=l2.next
        
		#traversing the 2 lists and checking the min. among them and adding that to the new lists
        while l1 and l2:
            if l1.val<=l2.val:
                new.next=l1
                new=l1
                l1=l1.next
            else:
                new.next=l2
                new=l2
                l2=l2.next
        
		#The last node     
        if l1:
            new.next=l1
        elif l2:
            new.next=l2
        return head
