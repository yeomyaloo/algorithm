import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        cnt = 0
        for i in jewels:
            cnt += freqs[i]
        return cnt
