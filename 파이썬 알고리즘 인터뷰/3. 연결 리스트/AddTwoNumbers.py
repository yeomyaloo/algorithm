# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    #연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        list: list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self,result : str) -> ListNode:
        prev: ListNode = None
        for i in result:
            node = ListNode(i)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReversedLinkedList(str(resultStr))
