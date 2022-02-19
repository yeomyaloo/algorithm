class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            # 첫 번째 인덱스는 while의 조건인 stack이 비어있지 않는 것을 충족하지 않아 바로 append 실행
            stack.append(i)

        return volume