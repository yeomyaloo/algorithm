import collections


class Solution(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for a,b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def DFS(a):
            while graph[a]:
                # 첫 번째 값을 읽어서 어휘순으로 방문한다.
                DFS(graph[a].pop())
            route.append(a)

        DFS("JFK")

        return route[::-1]