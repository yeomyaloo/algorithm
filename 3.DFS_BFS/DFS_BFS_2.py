#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문

def BFS(x,y):
    #큐 구현을 위해 덱 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 4가지 방향의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #미로 찾기의 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #괴물이 있어서 못가는 부분은(벽인 부분으로 생각) 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]
    


from collections import deque
#BFS를 사용할 땐 큐를 이용하는 것이 좋고, 큐는 리스트를 사용하는 것보다 라이브러리를 사용해야 메모리 효율성이 좋다.

n,m = map(int,input().split())

#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 가지 방향을 정의해준다. (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(BFS(0,0))
        
