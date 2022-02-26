class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        #런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next #두칸씩 구성
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev,next
        return not rev
