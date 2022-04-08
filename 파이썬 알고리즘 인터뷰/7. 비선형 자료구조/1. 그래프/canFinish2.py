import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        trace = set()
        visited = set()

        def DFS(i):
            #순환구조면 False
            if i in trace:
                return False
            #이미 방문한 노드라면 무조건 True를 돌려서 재탐색하지 않게 한다.
            if i in visited:
                return True

            trace.add(i)

            for y in graph[i]:
                #이미 방문했던 노드라면 False
                if not DFS(y):
                    return False

            #탐색 종료 후 방문 노드 추가
            visited.add(i)
            #탐색 종료 후 순환 노드 삭제
            trace.remove(i)

            return True

        for x in list(graph):
            if not DFS(x):
                return False
        return True