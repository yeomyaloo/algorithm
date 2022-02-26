class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for i in nums:
            pair.append(i)
            if len(pair) == 2:
                sum += min(pair)
                pair = []  # 핵심! 2개의 요소가 들어왔다면 작은 값을 sum에 주고 pair은 비어준다.

        return sum