from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = deque()
        for i in s:
            if i.isalnum():
                lst.append(i.lower())
        # 팰린드롬 여부 판별
        while len(lst) > 1:
            if lst.popleft() != lst.pop():
                return False
        return True
