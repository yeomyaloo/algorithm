class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def DFS(csum, index, path):
            #목표값 초과한 경우 탐색 종료
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                DFS(csum - candidates[i], i, path + [candidates[i]])

        DFS(target, 0, [])
        return result