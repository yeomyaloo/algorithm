class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        cnt = 0

        for i in stones:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1

        #갯수 합산
        for i in jewels:
            if i in freqs:
                cnt += freqs[i]
        return cnt