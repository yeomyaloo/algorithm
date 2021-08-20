#모험가 길드

n = int(input())
data = list(map(int,input().split()))
data.sort() #길드원을 공포도가 낮은 순서부터 오름차순으로 정렬 

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도가 낮은 길드원부터 하나씩 확인하며
    count+=1 #현재 그룹에 해당 모험가를 포함시키기
    if count > i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹결성
        result += 1 #총 그룹 수 증가시키기
        count = 0 #현재 그룹에 포함도니 모험가의 수 초기화하기.

print(result)        
    
