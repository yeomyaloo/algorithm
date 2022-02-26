class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i in range(len(nums)-1):
            if i % 2 == 0:
                sum += nums[i]
        return sum