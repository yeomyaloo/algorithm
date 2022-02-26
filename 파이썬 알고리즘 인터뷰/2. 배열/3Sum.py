#실패문제 !타임 아웃!!
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        answer.append([nums[i],nums[j],nums[k]])
        return answer