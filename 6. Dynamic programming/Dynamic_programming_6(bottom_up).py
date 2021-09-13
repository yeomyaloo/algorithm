import sys
input = sys.stdin.readline

n, m = map(int,input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

#계산된 결과를 저장하기 위한 DP 테이블 초기화

d = [10001]*(m+1)

#다이나믹 프로그래밍 진행(보텀업)
d[0] = 0

#점화식에 따라 다이나믹 프로그래밍 진행
for i in range(n): # i == 화폐단위 
    for j in range(coin[i],m+1): #j == 금액
     if d[j - coin[i]] != 10001: #(i-k)원을 만드는 경우가 존재하는 경우
         d[j] = min(d[j],d[j-coin[i]]+1)
#계산된 결과 출력
if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
    
