# 떡볶이 떡 만들기 
n, m = map(int,input().split()) # n=떡의 개수 / m=떡의 길이

array = list(map(int,input().split()))

start = 0 
end = max(array) #젤 큰 값이 끝값

result = 0

while(start <= end):
    total = 0
    mid = (start+end)//2
    for i in array:
        #잘랐을 때의 떡의 양 계산 (현재의 떡이 자르고자하는 크기보다 클때만 자를 수 있다.)
        if i > mid:
            total += i-mid
            
    # 떡의 양이 부족한 경우 더 많이 짜르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
        
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid #최대한 덜 잘랐을 때가 정답, 여기에 result를 기록
        start = mid + 1
        
print(result)
    
