from bisect import bisect_left, bisect_right

#값이 left_value, right_value인 데이터의 개수를 반환하는 함수
def count_by_range(a,left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index


n, x = map(int,input().split())
array = list(map(int,input().split()))

#값이 입력받은 x인 수를 n개 입력받은 리스트 array에서 찾기
count = count_by_range(array,x,x)


#찾고자 하는 수인 x가 array안에 없으면
if count == 0:
    print(-1)
#값이 x인 원소가 존재한다면
else:
    print(count)
