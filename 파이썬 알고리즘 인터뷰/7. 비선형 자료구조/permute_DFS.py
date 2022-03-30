class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def DFS(elements):
            #리프 노드일 때 결과 추가
            if len(elements) == 0:
                result.append(prev_elements[:])
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                DFS(next_elements)
                prev_elements.pop()
        DFS(nums)
        return result

