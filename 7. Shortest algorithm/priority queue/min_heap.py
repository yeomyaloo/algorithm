import heapq

#오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
        #힙푸시의 경우 특정 리스트에 어떤 데이터를 넣을 수 있다.
        #넣는 경우엔 그냥 들어온 순서대로 넣고 나올 때 가장 우선순위가 낮은 것부터 빼낸
        
        
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        #힙팝의 경우엔 리스트에서 데이터를 꺼낼 때 사용할 수 있다.
        
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
