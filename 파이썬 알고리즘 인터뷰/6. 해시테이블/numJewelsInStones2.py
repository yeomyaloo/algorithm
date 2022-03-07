import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        cnt = 0

        for i in stones:
            freqs[i] += 1

        #갯수 합산
        for i in jewels:
            cnt += freqs[i]
        return cnt