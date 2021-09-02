#DFS구현
graph = {}
f = open ('graph.txt', 'r')
aline = f.readline()
#n = 버택스의 수 / m = 엣지의 수
n, m = map(int,(aline.split()))


#그래프에 vertex를 저장. 
for i in range(n):
    graph[i+1] = []

for i in range(m): #그래프에 엣지 저장
    aline = f.readline()
    n1, n2 = map(int,aline.split(' '))
    print(n1,n2)

    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(n):
    graph[i+1].sort() #정렬

print(graph)
