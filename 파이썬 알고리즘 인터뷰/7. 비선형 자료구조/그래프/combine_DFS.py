class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def DFS(elements, start:int, k:int):
            if k == 0:
                result.append(elements[:])
                return

            #자신 이외의 모든 값을 고정하여 재귀 호출
            for i in range(start, n+1):
                elements.append(i)
                DFS(elements, i+1, k -1)
                elements.pop()
        DFS([],1,k)
        return result