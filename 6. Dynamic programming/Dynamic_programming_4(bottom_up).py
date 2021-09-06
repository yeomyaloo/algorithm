#개미 전사

n = int(input()) #식량창고의 개수
array = list(map(int,input().split())) #식량창소에 저장된 식량의 개수 K

#dp 테이블 초기화
d = [0] * 100

#다이나믹 프로그래밍 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] +array[i])

print(d[n-1])
