class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) ->str
        #팰린드롬 판별 및 투 포인터 확장
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return s[left+1:right]

        #해당 사항이 없을 땐 빠르게 리턴해준다.
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''

        for i in range(len(s)-1):
            result = max(result, expand(i,i+1),
                         expand(i,i+2), key=len)
        return result
