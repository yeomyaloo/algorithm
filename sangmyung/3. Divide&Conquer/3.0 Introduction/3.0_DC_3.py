# Binary search (Divide & Conquer)

def binary_search(s,e,array,x): #시작값 끝값 찾을 배열 찾을 수
    for i in range(len(array)):
        #첫값과 끝값이 같다면 그대로 return
        if s == e:
            if array[s] == x:
                return s

        m = (s+e)//2 #중간값을 통해서 왼쪽 오른쪽 나누기 위함
        
        if array[m] == x: #중간 자리에 있는 값이 찾는 값일 경우
            return m
        elif array[m] > x:
            return binary_search(s,m-1,array,x)
        else:
            return binary_search(m+1,e,array,x)
        

a = [1,2,3,5,9,7,6]
n= int(input("찾고자하는 값을 입력해주세요. "))

if binary_search(0,6,a,n) == False:
    print("찾는 값이 존재하지 않습니다.")
else:
    print(f"찾고자 하는 값 {n}을(를) {binary_search(0,6,a,n)}번째에서 찾았습니다!")
