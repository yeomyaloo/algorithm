# Bruteforce search (linear search)

def linear_search(s,e,array,x): #시작값 끝값 찾을 배열 찾을 수
    for i in range(len(array)):

        #찾는 값이 있을 경우 i번째에 있는 값을 돌려준다.
        if array[i] == x:
            return i
    return False

a = [1,2,3,5,9,7,6]
n= int(input("찾고자하는 값을 입력해주세요. "))

if linear_search(0,6,a,n) == False:
    print("찾는 값이 존재하지 않습니다.")
else:
    print(f"찾고자 하는 값 {n}을(를) {linear_search(0,6,a,n)}번째에서 찾았습니다!")
