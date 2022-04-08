import collections
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)

        #그래프 인접 리스트 구성
        for u,v,w in times:
            # u -> v로 가는 비용이 w라는 의미
            graph[u].append((v,w))

        #큐 변수: [(소요 시간, 정점)]
        q = [(0,k)]

        #거리 비교를 위한 변수
        distant = collections.defaultdict(int)

        while q:
            time, node = heapq.heappop(q)

            if node not in distant:
                distant[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q(alt, v))
        if len(distant) == n:
            return max(distant.values())
        return -1

