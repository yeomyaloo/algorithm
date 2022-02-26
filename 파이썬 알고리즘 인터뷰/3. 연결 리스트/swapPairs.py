class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            current.val , current.next.val = current.next.val, current.val
            current = current.next.next

        return head
    

