class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer =[]
        p = 1

        #왼쪽 곱셈
        for i in range(len(nums)):
            answer.append(p)
            p = nums[i] * p
        p = 1 #재사용을 위함

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * p
            p = p * nums[i]
        return answer