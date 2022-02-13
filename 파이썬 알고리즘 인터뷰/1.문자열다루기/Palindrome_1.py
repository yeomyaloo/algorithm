class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for i in s:
            if i.isalnum():
                lst.append(i.lower())
        # 팰린드롬 여부 판별
        while len(lst) > 1:
            if lst.pop(0) != lst.pop():
                return False
        return True
