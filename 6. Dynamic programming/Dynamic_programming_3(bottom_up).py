#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화(DP = Dynamic programming)
d = [0] * 100

#첫 번째 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

for i in range(3,n+1):
    d[i] = d[i-1]+d[i-2]
print(d[n])

