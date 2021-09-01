#이진 탐색 소스코드 구현( 반복문을 이용해서 )

def binary_search(array,target,start,end):
    while start <= end:
        mid = start + end // 2  #중간점

        #찾고자하는 값이 중간값일 경우
        if array[mid] == target:
            return mid

        #찾고자하는 값이 중간값보다 작은 경우 왼쪽에서 확인 
        elif array[mid] > target:
            end = mid - 1

        # 찾고자하는 값이 중간값보다 큰 경우 오른쪽에서 확인
        else:
            start = mid + 1
    return None

n, target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(f'찾고자하는 수 {target}은(는) {result + 1}번째에 존재합니다.') 
