class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def comp(node):
            if not node:
                return 0
            c=comp(node.next)
            if c==n:
                nxt=node.next.next
                node.next=nxt
            return c+1
        f=comp(head)
        if f==n:
            head=head.next
        return head
