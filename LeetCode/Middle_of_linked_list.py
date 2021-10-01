
# Method 1)
"""
Intuition and Algorithm
When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. When fast reaches the end of the list, slow must be in the middle.
"""
def middleNode(head: Optional[ListNode]):
        slow = fast =head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
