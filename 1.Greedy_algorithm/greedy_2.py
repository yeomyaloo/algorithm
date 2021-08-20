#1이 될 때까지

n, k = map(int,input().split())
cnt = 0

while True:
    #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k
    cnt += (n - target)
    n = target

    #n이 k보다 작을 때 (더이상 나눌 수 없을 때) 반복문을 탈출
    if n < k:
        break
    #k로 나누기
    cnt += 1
    n//=k
    
#마지막 남은 수를 1씩 빼주기
cnt += (n-1)
print(cnt)
